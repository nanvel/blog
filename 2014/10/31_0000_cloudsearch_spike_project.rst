Amazon CloudSearch spike project
================================

Gist: https://gist.github.com/nanvel/4f7696174ac3a9b3554c

.. code-block:: python

    """
    Search bebop series.
    """
    import arrow
    import json

    from tornado import options
    from tornado.httpclient import HTTPError, HTTPClient, HTTPRequest
    from tornado_botocore import Botocore
    from tvs import TVS


    DOMAIN_NAME = 'test-bebop-domain'
    API_VERSION = '2013-01-01'


    if __name__ == '__main__':
        options.parse_command_line()
        # create domain
        cs_create_domain = Botocore(
            service='cloudsearch', operation='CreateDomain',
            region_name='us-west-2')
        session = cs_create_domain.session
        try:
            # create domain, domain will be reused if already exists
            print cs_create_domain.call(domain_name=DOMAIN_NAME)
            # {  
            #    "DomainStatus":{  
            #       "DomainId":"240020657974/test-bebop-domain",
            #       "Created":true,
            #       "SearchService":{},
            #       "SearchInstanceCount":0,
            #       "DomainName":"test-bebop-domain",
            #       "DocService":{},
            #       "Deleted":false,
            #       "Processing":false,
            #       "RequiresIndexDocuments":false,
            #       "ARN":"arn:aws:cloudsearch:us-west-2:240020657974:domain/test-bebop-domain",
            #       "SearchPartitionCount":0
            #    },
            #    "ResponseMetadata":{  
            #       "RequestId":"38b0cba7-60f2-11e4-980e-6d6976ea3108"
            #    }
            # }
        except HTTPError as e:
            print e.response.body
        # configure fields
        cs_define_index_field = Botocore(
            service='cloudsearch', operation='DefineIndexField',
            region_name='us-west-2', session=session)
        # Fields:
        # - title - text + show in result
        # - airdate - uint
        # - genre - literal + facet enabled (or literal-array?)
        # - content - text
        FIELDS = [{
            'DomainName': DOMAIN_NAME,
            'IndexField': {
                'IndexFieldName': 'title',
                'IndexFieldType': 'text',
                'TextOptions': {
                    'HighlightEnabled': False,
                    'DefaultValue': 'untitled',
                    'ReturnEnabled': True,
                }
            }
        }, {
            'DomainName': DOMAIN_NAME,
            'IndexField': {
                'IndexFieldName': 'content',
                'IndexFieldType': 'text',
                'TextOptions': {
                    'HighlightEnabled': False,
                    'DefaultValue': '',
                    'ReturnEnabled': False,
                }
            }
        }, {
            'DomainName': DOMAIN_NAME,
            'IndexField': {
                'IndexFieldName': 'airdate',
                'IndexFieldType': 'int',
                'IntOptions': {
                    'DefaultValue': 946684800,
                }
            }
        }, {
            'DomainName': DOMAIN_NAME,
            'IndexField': {
                'IndexFieldName': 'genre',
                'IndexFieldType': 'literal-array',
                'LiteralArrayOptions': {
                    'DefaultValue': '',
                    'FacetEnabled': True,
                    'ReturnEnabled': False,
                    'SearchEnabled': True,
                }
            }
        }]
        try:
            for params in FIELDS:
                print cs_define_index_field.call(**params)
        except HTTPError as e:
            print e.response.body
        # add data
        batch = []
        for tv in TVS:
            batch.append({
                'type': 'add', 'id': tv['number'],
                'fields': {
                    'title': tv['title'],
                    'content': tv['content'],
                    'airdate': arrow.get(tv['airdate'], ['YYYY-MM-DD', 'MMMM D, YYYY']).timestamp,
                    'genre': tv['genre'],
                }
            })
        # get document and search endpoints
        cs_describe_domains = Botocore(
            service='cloudsearch', operation='DescribeDomains',
            region_name='us-west-2', session=session)
        response = cs_describe_domains.call(domain_names=[DOMAIN_NAME])
        # {  
        #    "DomainStatusList":[  
        #       {  
        #          "DomainId":"240020657974/test-bebop-domain",
        #          "Created":true,
        #          "SearchService":{  
        #             "Endpoint":"search-test-bebop-domain-kmvxd5zzot4opij6zvb6okvrma.us-west-2.cloudsearch.amazonaws.com"
        #          },
        #          "SearchInstanceCount":1,
        #          "DomainName":"test-bebop-domain",
        #          "DocService":{  
        #             "Endpoint":"doc-test-bebop-domain-kmvxd5zzot4opij6zvb6okvrma.us-west-2.cloudsearch.amazonaws.com"
        #          },
        #          "SearchInstanceType":"search.m1.small",
        #          "Deleted":false,
        #          "Processing":false,
        #          "RequiresIndexDocuments":true,
        #          "ARN":"arn:aws:cloudsearch:us-west-2:240020657974:domain/test-bebop-domain",
        #          "SearchPartitionCount":1
        #       }
        #    ],
        #    "ResponseMetadata":{  
        #       "RequestId":"7993ac9b-6101-11e4-8510-8ffcccb94f21"
        #    }
        # }
        search_endpoint = response['DomainStatusList'][0]['SearchService']['Endpoint']
        document_endpoint = response['DomainStatusList'][0]['DocService']['Endpoint']
        httpclient = HTTPClient()
        # reindex
        cs_index_documents = Botocore(
            service='cloudsearch', operation='IndexDocuments',
            region_name='us-west-2', session=session)
        print cs_index_documents.call(domain_name=DOMAIN_NAME)
        # wait unil reindex complete
        # add documents
        url = 'http://{document_endpoint}/{api_version}/documents/batch'.format(
            document_endpoint=document_endpoint,
            api_version=API_VERSION)
        try:
            request = HTTPRequest(
                url=url, body=json.dumps(batch),
                headers={'Content-Type': 'application/json'}, method='POST')
            request.params = None
            cs_describe_domains.endpoint.auth.add_auth(request=request)
            response = httpclient.fetch(request=request)
            print response.body
        except HTTPError as e:
            print e.response.body
        # search
        url = 'http://{search_endpoint}/{api_version}/search?q=bebop'.format(
            search_endpoint=search_endpoint, api_version=API_VERSION)
        request = HTTPRequest(
            url=url, headers={'Content-Type': 'application/json'},
            method='GET')
        request.params = None
        cs_describe_domains.endpoint.auth.add_auth(request=request)
        response = httpclient.fetch(request=request)
        print response.body
        # {  
        #    "status":{  
        #       "rid":"st/UtJYpAAoghec=",
        #       "time-ms":82
        #    },
        #    "hits":{  
        #       "found":12,
        #       "start":0,
        #       "hit":[  
        #          {  
        #             "id":"3",
        #             "fields":{  
        #                "airdate":"910396800",
        #                "title":"Honky Tonk Women"
        #             }
        #          },
        #          {  
        #             "id":"18",
        #             "fields":{  
        #                "airdate":"920073600",
        #                "title":"Speak Like a Child"
        #             }
        #          },
        #          ...
        #       ]
        #    }
        # }

.. info::
    :tags: AWS, CloudSearch
    :place: Kyiv, Ukraine

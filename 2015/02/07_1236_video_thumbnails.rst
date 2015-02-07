Get youtube/vimeo/vevo/vine videos thumbnails
=============================================

.. code-block:: python

    import re
    import urllib2


    class Thumbnail(object):

        YOUTUBE_THUMBNAIL_URL = 'https://i.ytimg.com/vi/{video_id}/hqdefault.jpg'
        VEVO_VIDEO_URL = 'http://www.vevo.ly/{video_id}'
        VEVO_THUMBNAIL_URL_REGEXP1 = re.compile('"thumbnailUrl":"(.+?)"')
        VEVO_THUMBNAIL_URL_REGEXP2 = re.compile('link itemprop="thumbnailUrl" href="(.+?)"')
        VINE_VIDEO_URL = 'http://vine.co/v/{video_id}'
        VINE_THUMBNAIL_URL_REGEXP = re.compile('"thumbnailUrl": "(.+?)"')
        VIMEO_DATA_URL = 'http://vimeo.com/api/v2/video/{video_id}.json'
        VIMEO_THUMBNAIL_URL_REGEXT = re.compile('"thumbnail_large":"(.+?)"')

        @classmethod
        def youtube(cls, video_id):
            return cls.YOUTUBE_THUMBNAIL_URL.format(video_id=video_id)

        @classmethod
        def vimeo(cls, video_id):
            vimeo_url = cls.VIMEO_DATA_URL.format(video_id=video_id)
            data = urllib2.urlopen(vimeo_url).read()
            results = cls.VIMEO_THUMBNAIL_URL_REGEXT.findall(data)
            if results:
                return results[0].replace('\\/', '/')

        @classmethod
        def vevo(cls, video_id):
            video_url = cls.VEVO_VIDEO_URL.format(video_id=video_id)
            req = urllib2.Request(video_url)
            req.add_header(
                'User-Agent',
                'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            page = urllib2.urlopen(req).read()
            # request from zone where vevo is available
            results = cls.VEVO_THUMBNAIL_URL_REGEXP1.findall(page)
            if not results:
                # if vevo is unavailable, it may be open on youtube
                results = cls.VEVO_THUMBNAIL_URL_REGEXP2.findall(page)
            if results:
                return results[0]

        @classmethod
        def vine(cls, video_id):
            vine_url = cls.VINE_VIDEO_URL.format(video_id=video_id)
            req = urllib2.Request(vine_url)
            req.add_header(
                'User-Agent',
                'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
            page = urllib2.urlopen(req).read()
            results = cls.VINE_THUMBNAIL_URL_REGEXP.findall(page)
            if results:
                return results[0].replace('\\/', '/')


    if __name__ == '__main__':
        print Thumbnail.youtube(video_id='p8KwGIyHmhM')
        print Thumbnail.vimeo(video_id='45370040')
        print Thumbnail.vevo(video_id='x9fMmU')
        print Thumbnail.vine(video_id='OUBbPBrh2qH')


.. info::
    :tags: Python, VideoThumbnails
    :place: Phuket, Thailand

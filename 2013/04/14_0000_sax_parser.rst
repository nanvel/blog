SAX parser
==========

.. image:: https://raw.githubusercontent.com/nanvel/blog/master/2013/04/sax.png
    :width: 600px
    :alt: SAX XML parser
    :align: left

`SAX <http://en.wikipedia.org/wiki/Simple_API_for_XML>`__ - Simple API for XML.

SAX parser much more lightweight than DOM parser. So in case of large data structures with great amount of nodes selecting SAX is the only one right decision.
Python out of box already has all of You need to build SAX parser.

.. code-block:: python

    import sys

    from xml.sax import handler, parse


    class MyContentHandler(handler.ContentHandler):

        def __init__(self, out=sys.stdout):
            handler.ContentHandler.__init__(self)
            self._out = out

        def startDocument(self):
            pass

        def startElement(self, name, attrs):
            self.content = ''

        def characters(self, content):
            self.content += content

        def endElement(self, name):
            self._out.write('%s = %s\n' % (name, self.content))

        def endDocument(self):
            pass


    def main():
        """
        # example.xml
        <ResultSet>
            <Result id="1">
                <name>
                    Electromaster
                </name>
            </Result>
            <Result id="2">
                <name>
                    When You Work Under The Sun, You Need To Stay Rehydrated
                </name>
            </Result>
            <Result id="3">
                <name>
                    Tokiwadai is Targeted
                </name>
            </Result>
        </ResultSet>

        Result:
        python parser.py 
        name = Electromaster
        Result = Electromaster
        name = When You Work Under The Sun, You Need To Stay Rehydrated
        Result = When You Work Under The Sun, You Need To Stay Rehydrated
        name = Tokiwadai is Targeted
        Result = Tokiwadai is Targeted
        ResultSet = Tokiwadai is Targeted
        """
        f = open('example.xml')
        parse(f, MyContentHandler())


    if __name__ == "__main__":
        main()

Also can be useful: http://docs.python.org/dev/library/xml.dom.pulldom.html

Links:
    - http://en.wikipedia.org/wiki/Simple_API_for_XML
    - http://docs.python.org/2/library/xml.sax.html
    - http://mail.python.org/pipermail/python-dev/2000-October/009946.html

.. info::
    :tags: XML, SAX
    :place: Alchevs'k, Ukraine

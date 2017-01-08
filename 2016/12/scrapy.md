labels: Draft
        Scrapers
created: 2016-12-16T21:04
modified: 2016-12-18T10:12
place: Phuket, Thailand
comments: true

# Scrapy

[TOC]

```bash
>>> response.css('title::text').re(r'Quotes.*')
['Quotes to Scrape']
>>> response.css('title::text').re(r'Q\w+')
['Quotes']
>>> response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']
```

## Parse

urljoin:
```python
next_page = response.urljoin('/page/2/')
yield scrapy.Request(next_page, callback=self.parse)
```

### Form request

```python
def parse(self, response):
    return scrapy.FormRequest.from_response(
        response,
        formdata={'username': 'john', 'password': 'secret'},
        callback=self.after_login
    )
```

## XPath

[Concise XPath](http://plasmasturm.org/log/xpath101/).
[XPath tutorial](http://www.zvon.org/comp/r/tut-XPath_1.html).
[Scrapy best practices](https://blog.scrapinghub.com/2014/07/17/xpath-tips-from-the-web-scraping-trenches/) on The scrapinghub blog.

```bash
>>> from scrapy.selector import Selector
>>> from scrapy.http import HtmlResponse


>>> body = '<html><body><span>good</span></body></html>'
>>> Selector(text=body).xpath('//span/text()').extract()
[u'good']

>>> response = HtmlResponse(url='http://example.com', body=body)
>>> response.selector.xpath('//span/text()').extract()
[u'good']

>>> response.selector.xpath('//span/text()').extract_first()
u'good'
```

Conditions separated by "/" are known as steps.
Condition inside "[]" is known as predicate.

## Commands

```bash
scrapy startproject myproject [project_dir]
scrapy genspider mydomain mydomain.com
```

Global commands:

- startproject
- genspider
- settings
- runspider
- shell
- fetch
- view
- version

Project-only commands:

- crawl
- check
- list
- edit
- parse
- bench

Running a spider:

`scrapy crawl <spidername> -s CLOSESPIDER_ITEMCOUNT=10`

## Debug

```python
from scrapy.utils.response import open_in_browser
open_in_browser(response)

from scrapy.shell import inspect_response
inspect_response(response, self)
```

## Logging

```python
import scrapy


class MySpider(scrapy.Spider):

	# ...

	def parse(self, response):
    	self.logger.info('A response from %s just arrived!', response.url)
```

## Shell

```bash
scrapy shell 'http://quotes.toscrape.com/page/1/'
```

## Settings

See [https://doc.scrapy.org/en/1.2/topics/settings.html#built-in-settings-reference](https://doc.scrapy.org/en/1.2/topics/settings.html#topics-settings-ref).

## Items and Item loaders

[Items](https://doc.scrapy.org/en/1.2/topics/items.html) provide the container of scraped data, while [Item Loaders](https://doc.scrapy.org/en/1.2/topics/loaders.html) provide the mechanism for populating that container.

## Best practices

### Spider name

If the spider scrapes a single domain, a common practice is to name the spider after the domain, with or without the TLD. So, for example, a spider that crawls mywebsite.com would often be called mywebsite.

## Vocabulary

### Scraping

The main goal in scraping is to extract structured data from unstructured sources.

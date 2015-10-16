labels: Blog
        Scrappers
created: 2014-03-29T00:00
place: Starobilsk, Ukraine

# Scrap NAICS codes and save them to sqlite database

The task is to get all NAICS codes with titles from [http://www.naics.com/search/](http://www.naics.com/search/) and save them to sqlite database.

I'll use [Beautifu](http://www.crummy.com/software/BeautifulSoup/) soup for scraping. See also:

- [scrapy](http://scrapy.org/)
- [mechanize](http://wwwsearch.sourceforge.net/mechanize/)

Install requirements:
```bash
pip install beautifulsoup4
```

Code:
```python
import os.path
import sqlite3
import urllib2

from bs4 import BeautifulSoup


TARGET_URL = 'http://www.naics.com/search/'


def parse_page(cur, url):
    f = urllib2.urlopen(url)
    soup = BeautifulSoup(f.read())
    table = soup.find('table')
    for tr in table.find_all('tr'):
        tds = tr.find_all('td')
        if tds:
            code = tds[0].get_text()
            if len(code) != 6:
                continue
            title = tds[1].get_text()
            print code, title
            cur.executescript(u"""
                INSERT INTO Codes(Code, Title) VALUES({code}, "{title}");
            """.format(code=code, title=title))


def main():
    # init db
    db_path = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), 'naics.sqlite3')
    con = sqlite3.connect(db_path)
    with con:
        cur = con.cursor()
        cur.executescript("""
            DROP TABLE IF EXISTS Codes;
            CREATE TABLE Codes(Code INT PRIMARY KEY, Title TEXT);
        """)
        # scrap
        f = urllib2.urlopen(TARGET_URL)
        soup = BeautifulSoup(f.read())
        n = 0
        table = soup.find(
            'h4',
            text='NAICS CODE DRILL DOWN TABLE').next_sibling.find('table')
        for tr in table.find_all('tr'):
            tds = tr.find_all('td')
            if tds:
                parse_page(cur=cur, url=tds[0].find('a').get('href'))


if __name__ == '__main__':
    main()
```

Result:
```bash
sqlite3 naics.sqlite3
sqlite> select * from Codes where code like '111%';
111110|Soybean Farming
111120|Oilseed (except Soybean) Farming
...
111940|Hay Farming
111991|Sugar Beet Farming
111992|Peanut Farming
111998|All Other Miscellaneous Crop Farming
sqlite> .q
```

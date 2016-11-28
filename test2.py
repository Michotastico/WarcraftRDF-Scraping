#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2

from bs4 import BeautifulSoup

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"

base_url = 'http://wowwiki.wikia.com'
page = urllib2.urlopen("http://wowwiki.wikia.com/wiki/Category:Major_characters")
entity = BeautifulSoup(page, 'html.parser')
columns = entity.find('table').find_all('td')

for col in columns:
    urls = col.find_all('a', href=True)
    for url in urls:
        if url.text == u'Major characters':
            continue
        print base_url + url['href'], url.text

print "end"
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

import unicodedata
import urllib2

from bs4 import BeautifulSoup

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"

BASE_URL = 'http://wowwiki.wikia.com'


def camel_case_split(identifier):
    matches = re.finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return " ".join([m.group(0) for m in matches])


def clean_string(string):
    return_string = string.strip('\n').strip().replace('\n', " ")
    return_string = unicodedata.normalize("NFKD", return_string)
    if re.search(r"\d+,\d+,\d*", return_string) is None:
        return_string = re.sub(r"\d+", "", return_string)
    return_string = re.sub(r"\[\d*\w*\]", "", return_string)
    return_string = camel_case_split(return_string)
    return return_string


def parse_page(url_page):
    summary = dict()
    page = urllib2.urlopen(url_page)
    entity = BeautifulSoup(page, 'html.parser')
    name = entity.h1.text

    entity_summary = entity.find('table', {'class':'darktable'})

    rows = entity_summary.find_all('tr')

    alias = clean_string(rows[0].text)
    next_image_index = 2
    try:
        image = rows[1].img['data-src']
    except:
        try:
            image = rows[1].img['src']
        except:
            image = rows[2].img['data-src']
            next_image_index += 1

    summary['name'] = name
    summary['alias'] = alias
    summary['image'] = image

    rows = rows[next_image_index:]
    for row in rows:
        row = row.find_all('td')
        if len(row) != 2:
            continue
        subject, answer = row
        subject = clean_string(subject.text)
        if subject in [u'Relative(s)', u'Mentor(s)', u'Comp(s)', u'Student(s)']:
            people = list(filter((lambda x: x['href'][0] != u'#'), answer.find_all('a', href=True)))
            answer = list(map(lambda x: (BASE_URL + x['href'], x.text), people))
        else:
            answer = clean_string(answer.text)

        summary[subject] = answer

    return summary


def get_major_characters():
    base_url = BASE_URL
    page = urllib2.urlopen("http://wowwiki.wikia.com/wiki/Category:Major_characters")
    entity = BeautifulSoup(page, 'html.parser')
    columns = entity.find('table').find_all('td')

    return_list = list()

    for col in columns:
        urls = col.find_all('a', href=True)
        for url in urls:
            if url.text in [u'Major characters', u'Dragon Aspects']:
                continue
            return_list.append((base_url + url['href'], url.text))

    return return_list

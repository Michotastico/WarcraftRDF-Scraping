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
        image = rows[2].img['data-src']
        next_image_index += 1

    summary['name'] = name
    summary['alias'] = alias
    summary['image'] = image

    rows = rows[next_image_index:-1]
    for row in rows:
        subject, answer = row.find_all('td')
        subject = clean_string(subject.text)
        answer = clean_string(answer.text)
        summary[subject] = answer

    return summary

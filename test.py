#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint

from utils.scraping import parse_page

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"


urls = ["http://wowwiki.wikia.com/wiki/Arthas_Menethil",
        "http://wowwiki.wikia.com/wiki/Thrall"]
pprint(parse_page(urls[0]))
"""
for url in urls:
    parsed_entity = parse_page(url[0])
    pprint(parsed_entity)
"""
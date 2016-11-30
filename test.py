#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint

from utils.scraping import *

__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"

urls = get_major_characters()

for url in urls:
    parsed_entity = parse_page(url[0])
    pprint(parsed_entity)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.scraping import *
from utils.rdfy import *
from utils.connection import *

"""Get the major characters, generate the queries and send it to the server.
After that append new characters to parse (usually minor characters)."""
to_do_chars = get_major_characters()
done_chars = {}
already_counter = 0
while to_do_chars:
    scraping_char = to_do_chars.pop(0)

    print already_counter, scraping_char
    already_counter += 1

    if not done_chars.get(scraping_char[1], False):

        script, new_chars = scrap_to_rdf(scraping_char[0], parse_page(scraping_char[0]))
        try:
            update_sparql_server(script)

            to_do_chars.extend(new_chars)

            done_chars[scraping_char[1]] = scraping_char[0]
        except:
            print script

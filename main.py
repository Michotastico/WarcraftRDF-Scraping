from utils.scraping import *
from utils.rdfy import *
from utils.connection import *

to_do_chars = get_major_characters()
done_chars = {}

while to_do_chars:
    scraping_char = to_do_chars.pop(0)


    print scraping_char
    if not done_chars.get(scraping_char[1], False):

        script, new_chars = scrap_to_rdf(scraping_char[0], parse_page(scraping_char[0]))

        update_sparql_server(script)

        to_do_chars.extend(new_chars)

        done_chars[scraping_char[1]] = scraping_char[0]

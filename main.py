from utils.scraping import *


to_do_chars = get_major_characters()
done_chars = {}

while to_do_chars:
    scraping_char = to_do_chars.pop(0)

    if not done_chars.get(scraping_char[1], False):
        #TODO scrapping
        done_chars[scraping_char[1]] = scraping_char[0]

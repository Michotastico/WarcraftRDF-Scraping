from utils.scraping import *


def scrap_to_rdf(url, data):



    url_string = "<" + url + ">"
    print url_string
    name_string = data['name']
    print name_string

    url_insert = url_string +' foaf:name '
    url_insert = url_insert + "\"" + name_string + "\""
    url_insert = url_insert + ' .\n'
    print url_insert

    alias_string = data['alias']
    print alias_string
    gender_string = data['Gender']
    print gender_string




    a = """PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema>
    INSERT DATA {
    %s
    }; """ % (url_insert)
    print a





scrap_to_rdf("http://wowwiki.wikia.com/wiki/Arthas_Menethil", parse_page("http://wowwiki.wikia.com/wiki/Arthas_Menethil"))
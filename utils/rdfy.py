from utils.scraping import *


def scrap_to_rdf(url, data):


    final_insert = list()

    #generar entidad  y agregarle nombre
    name_string = data['name']
    entity_string = "warcraft:" + name_string.replace(" ", "_")
    name_string = "\"" + name_string + "\""
    final_insert.append(entity_string + ' foaf:name ' + name_string + " .")
    final_insert.append(entity_string + ' a warcraft:Character .' )

    #buscar url y agregarlo
    url_string = "<" + url + ">"
    final_insert.append(entity_string + ' foaf:isPrimaryTopicOf ' + url_string + ' .')

    #buscar alias y agregarlo
    alias_string = data['alias']
    final_insert.append(entity_string + ' foaf:nick ' + "\"" + alias_string + "\"" + ' .')

    #buscar genero y agregarlo
    gender_string = data['Gender']
    final_insert.append(entity_string + ' foaf:gender ' + "\"" + gender_string + "\"" + ' .')

    #buscar imagen y agregarla
    image_string = data['image']
    final_insert.append(entity_string + ' foaf:img ' + "<" + image_string + ">" + ' .')




    #juntando todas los triples creados
    final_insert = "\n".join(final_insert)

    a = """PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema>
PREFIX warcraft: <http://www.warcraft.rdf/>
INSERT DATA {
%s
}; """ % (final_insert)
    print a





scrap_to_rdf("http://wowwiki.wikia.com/wiki/Arthas_Menethil", parse_page("http://wowwiki.wikia.com/wiki/Arthas_Menethil"))
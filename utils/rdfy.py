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
    if data.get('alias', False):
        alias_string = data['alias']
        final_insert.append(entity_string + ' foaf:nick ' + "\"" + alias_string + "\"" + ' .')

    #buscar genero y agregarlo
    if data.get('Gender', False):
        gender_string = data['Gender']
        final_insert.append(entity_string + ' foaf:gender ' + "\"" + gender_string + "\"" + ' .')

    #buscar imagen y agregarla
    if data.get('image', False):
        image_string = data['image']
        final_insert.append(entity_string + ' foaf:img ' + "<" + image_string + ">" + ' .')

    #buscar mentores y agregarlos
    if data.get('Mentor(s)', False):
        mentors = data['Mentor(s)']
        for mentor in mentors:
            final_insert.append(entity_string + ' warcraft:hasMentor warcraft:' + mentor[1].replace(" ", "_") + " .")

    #buscar calses y agregarlas
    if data.get('Character class', False):
        classes = data['Character class']
        for cc in classes:
            final_insert.append(entity_string + ' warcraft:Class ' + cc + ' .')

    #buscar titulos y agregarlos
    if data.get('Title', False):
        titles = data['Title']
        for title in titles:
            final_insert.append(entity_string + ' warcraft:Title ' + title + ' .')

    #buscar raza y agregarla
    if data.get('Race', False):
        races = data['Race']
        for race in races:
            final_insert.append(entity_string + ' warcraft:Race ' + race[1] + ' .')

    #buscar afiliacion y agregarla
    if data.get('Affiliation', False):
        affiliations = data['Affiliation']
        for aff in affiliations:
            final_insert.append(entity_string + ' warcraft:AffiliatedTo ' + aff[1] + ' .')

    #buscar nivel y agregarlo
    if data.get('Level', False):
        final_insert.append(entity_string + ' warcraft:Level ' + data['Level'] + ' .')

    #buscar via y agregarla
    if data.get('Health', False):
        final_insert.append(entity_string + ' warcraft:Health ' + data['Health'] + ' .')

    #buscar mana y agregarla
    if data.get('Mana', False):
        final_insert.append(entity_string + ' warcraft:Mana ' + data['Mana'] + ' .')
















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
from utils.scraping import *


def remove_comillas(str):
    return str.replace("\"", " ")


def scrap_to_rdf(url, data):

    final_insert = list()
    aditional_chars = list()

    # generar entidad  y agregarle nombre
    name_string = data['name']
    entity_string = "warcraft:" + name_string.replace(" ", "_").replace("'", "_")
    name_string = "\"" + name_string + "\""
    final_insert.append(entity_string + ' foaf:name ' + name_string + " .")
    final_insert.append(entity_string + ' a warcraft:Character .')

    # buscar url y agregarlo
    url_string = "<" + url + ">"
    final_insert.append(entity_string + ' foaf:isPrimaryTopicOf ' + url_string + ' .')

    # buscar alias y agregarlo
    if data.get('alias', False):
        alias_string = data['alias']
        final_insert.append(entity_string + ' foaf:nick ' + "\"" + remove_comillas(alias_string) + "\"" + ' .')

    # buscar genero y agregarlo
    if data.get('Gender', False):
        gender_string = data['Gender']
        final_insert.append(entity_string + ' foaf:gender ' + "\"" + remove_comillas(gender_string) + "\"" + ' .')

    # buscar imagen y agregarla
    if data.get('image', False):
        image_string = data['image']
        final_insert.append(entity_string + ' foaf:img ' + "<" + image_string + ">" + ' .')

    # buscar clases y agregarlas
    if data.get('Character class', False):
        classes = data['Character class']
        for cc in classes:
            final_insert.append(entity_string + ' warcraft:Class \"' + remove_comillas(cc) + '\" .')

    # buscar titulos y agregarlos
    if data.get('Title', False):
        titles = data['Title']
        for title in titles:
            final_insert.append(entity_string + ' warcraft:Title \"' + remove_comillas(title) + '\" .')

    # buscar raza y agregarla
    if data.get('Race', False):
        races = data['Race']
        for race in races:
            final_insert.append(entity_string + ' warcraft:Race \"' + remove_comillas(race[1]) + '\" .')

    # buscar afiliacion y agregarla
    if data.get('Affiliation', False):
        affiliations = data['Affiliation']
        for aff in affiliations:
            final_insert.append(entity_string + ' warcraft:AffiliatedTo \"' + remove_comillas(aff[1]) + '\" .')

    # buscar nivel y agregarlo
    if data.get('Level', False):
        final_insert.append(entity_string + ' warcraft:Level \"' + remove_comillas(data['Level']) + '\" .')

    # buscar vida y agregarla
    if data.get('Health', False):
        final_insert.append(entity_string + ' warcraft:Health \"' + remove_comillas(data['Health']) + '\" .')

    # buscar mana y agregarla
    if data.get('Mana', False):
        final_insert.append(entity_string + ' warcraft:Mana \"' + remove_comillas(data['Mana']) + '\" .')

    # buscar alineacion y agregarla
    if data.get('Alignment', False):
        alignments = data['Alignment']
        for alignment in alignments:
            final_insert.append(entity_string + ' warcraft:Alignment \"' + remove_comillas(alignment) + '\" .')

    # buscar ubicaciones y agregarla
    if data.get('Location', False):
        locations = data['Location']
        for location in locations:
            final_insert.append(entity_string + ' warcraft:LocatedIn \"' + remove_comillas(location) + '\" .')

    # buscar posiciones y agregarla
    if data.get('Position', False):
        positions = data['Position']
        for position in positions:
            final_insert.append(entity_string + ' warcraft:Position \"' + remove_comillas(position) + '\" .')

    # buscar status y agregarlo
    if data.get('Status', False):
        status = data['Status']
        for s in status:
            final_insert.append(entity_string + ' warcraft:Status \"' + remove_comillas(s) + '\" .')

    # buscar mentores y agregarlos
    if data.get('Mentor(s)', False):
        mentors = data['Mentor(s)']
        for mentor in mentors:
            final_insert.append(entity_string +
                                ' warcraft:hasMentor warcraft:' + mentor[1].replace(" ", "_").replace("'", "_") + " .")
            aditional_chars.append((mentor[0], mentor[1]))

    # buscar alumnos y agregarlos
    if data.get('Student(s)', False):
        students = data['Student(s)']
        for student in students:
            final_insert.append(entity_string +
                                ' warcraft:hasStudent warcraft:' + student[1].replace(" ", "_").replace("'", "_") + " .")
            aditional_chars.append((student[0], student[1]))

    # buscar companions y agregarlos
    if data.get('Comp(s)', False):
        companions = data['Comp(s)']
        for companion in companions:
            final_insert.append(
                entity_string +
                ' warcraft:hasCompanion warcraft:' + companion[1].replace(" ", "_").replace("'", "_") + " .")

    # buscar relatives y agregarlos
    if data.get('Relative(s)', False):
        relatives = data['Relative(s)']
        for r in relatives:
            # por ahora son todos relatives no mas, ahi vemos si agregamos los tags mas importantes
            final_insert.append(entity_string +
                                ' warcraft:Relative warcraft:' + r[1].replace(" ", "_").replace("'", "_") + " .")
            aditional_chars.append((r[0], r[1]))

    # juntando todos los triples creados
    final_insert = "\n".join(final_insert)

    insertion_script = """PREFIX foaf:  <http://xmlns.com/foaf/0.1/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema>
PREFIX warcraft: <http://www.warcraft.rdf/>
INSERT DATA {
%s
}; """ % final_insert

    #print insertion_script

    return insertion_script, aditional_chars

#s = "http://wowwiki.wikia.com/wiki/Archimonde"
#scrap_to_rdf(s, parse_page(s))
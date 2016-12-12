from utils.scraping import *


def sanitize_query(string):
    return string.replace("\"", " ").replace("'", " ").replace("\n", " ").strip()


def parse_tags(tag):
    return_tag = tag.replace(" ", "_").replace("'", "_").replace("\"", " ").replace("(", "").replace(")", "")
    return_tag = return_tag.replace("/", "_").replace("&", "").strip()
    return return_tag


def scrap_to_rdf(url, data):

    final_insert = list()
    aditional_chars = list()

    # generar entidad  y agregarle nombre
    name_string = data['name']
    entity_string = "warcraft:" + parse_tags(name_string)
    name_string = "\"" + name_string + "\""
    final_insert.append(entity_string + ' foaf:name ' + name_string + " .")
    final_insert.append(entity_string + ' a warcraft:Character .')

    # buscar url y agregarlo
    url_string = "<" + url + ">"
    final_insert.append(entity_string + ' foaf:isPrimaryTopicOf ' + url_string + ' .')

    # buscar alias y agregarlo
    if data.get('alias', False):
        alias_string = data['alias']
        final_insert.append(entity_string + ' foaf:nick ' + "\"" + sanitize_query(alias_string) + "\"" + ' .')

    # buscar genero y agregarlo
    if data.get('Gender', False):
        gender_string = data['Gender']
        final_insert.append(entity_string + ' foaf:gender ' + "\"" + sanitize_query(gender_string) + "\"" + ' .')

    # buscar imagen y agregarla
    if data.get('image', False):
        image_string = data['image']
        final_insert.append(entity_string + ' foaf:img ' + "<" + image_string + ">" + ' .')

    # buscar clases y agregarlas
    if data.get('Character class', False):
        classes = data['Character class']
        for cc in classes:
            final_insert.append(entity_string + ' warcraft:Class \"' + sanitize_query(cc) + '\" .')

    # buscar titulos y agregarlos
    if data.get('Title', False):
        titles = data['Title']
        for title in titles:
            final_insert.append(entity_string + ' warcraft:Title \"' + sanitize_query(title) + '\" .')

    # buscar raza y agregarla
    if data.get('Race', False):
        races = data['Race']
        for race in races:
            final_insert.append(entity_string + ' warcraft:Race \"' + sanitize_query(race[1]) + '\" .')

    # buscar afiliacion y agregarla
    if data.get('Affiliation', False):
        affiliations = data['Affiliation']
        for aff in affiliations:
            final_insert.append(entity_string + ' warcraft:AffiliatedTo \"' + sanitize_query(aff[1]) + '\" .')

    # buscar nivel y agregarlo
    if data.get('Level', False):
        final_insert.append(entity_string + ' warcraft:Level \"' + sanitize_query(data['Level']) + '\" .')

    # buscar vida y agregarla
    if data.get('Health', False):
        final_insert.append(entity_string + ' warcraft:Health \"' + sanitize_query(data['Health']) + '\" .')

    # buscar mana y agregarla
    if data.get('Mana', False):
        final_insert.append(entity_string + ' warcraft:Mana \"' + sanitize_query(data['Mana']) + '\" .')

    # buscar alineacion y agregarla
    if data.get('Alignment', False):
        alignments = data['Alignment']
        for alignment in alignments:
            final_insert.append(entity_string + ' warcraft:Alignment \"' + sanitize_query(alignment) + '\" .')

    # buscar ubicaciones y agregarla
    if data.get('Location', False):
        locations = data['Location']
        for location in locations:
            final_insert.append(entity_string + ' warcraft:LocatedIn \"' + sanitize_query(location) + '\" .')

    # buscar posiciones y agregarla
    if data.get('Position', False):
        positions = data['Position']
        for position in positions:
            final_insert.append(entity_string + ' warcraft:Position \"' + sanitize_query(position) + '\" .')

    # buscar status y agregarlo
    if data.get('Status', False):
        status = data['Status']
        for s in status:
            final_insert.append(entity_string + ' warcraft:Status \"' + sanitize_query(s) + '\" .')

    # buscar mentores y agregarlos
    if data.get('Mentor(s)', False):
        mentors = data['Mentor(s)']
        for mentor in mentors:
            final_insert.append(entity_string +
                                ' warcraft:hasMentor warcraft:' + parse_tags(mentor[1]) + " .")
            aditional_chars.append((mentor[0], mentor[1]))

    # buscar alumnos y agregarlos
    if data.get('Student(s)', False):
        students = data['Student(s)']
        for student in students:
            final_insert.append(entity_string +
                                ' warcraft:hasStudent warcraft:' + parse_tags(student[1]) + " .")
            aditional_chars.append((student[0], student[1]))

    # buscar companions y agregarlos
    if data.get('Comp(s)', False):
        companions = data['Comp(s)']
        for companion in companions:
            final_insert.append(
                entity_string +
                ' warcraft:hasCompanion warcraft:' + parse_tags(companion[1]) + " .")

    # buscar relatives y agregarlos
    if data.get('Relative(s)', False):
        relatives = data['Relative(s)']
        for r in relatives:
            # por ahora son todos relatives no mas, ahi vemos si agregamos los tags mas importantes
            relative_tag = parse_tags(r[1])
            if relative_tag in [u'*']:
                continue
            final_insert.append(entity_string +
                                ' warcraft:Relative warcraft:' + relative_tag + " .")
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
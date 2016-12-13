# Warcraft RDF - Scraping

As part of the course CC6202 - Linked Data, we decided to generate a method to extract and generate a non relational database of Warcraft, fundamentally over the major characters and the relations between them.

### Version
1.0.0

### Tech
The project was realized with Python for the scraping work, the generation of SPARQL update queries and the connection with the database. For the database we used [Jena] and [Fuseki].

The project uses the following libraries (As indicated on the requirements file):
* [BeautifulSoup4] - Python library to scrape webpages.
* [SPARQLWrapper] - Python library to connect with SPARQL databases.

The project itself is open source with a [public repository][scraper] on GitHub.


### Run & Configuration

The project itself was made using [Pycharm], but It can be run directly from console.

```sh
$ python main.py
```

But first we need to configure the connection with the database on the file **utils/connection.py**, replacing the respective URL.
```sh
UPDATE_URL = "http://127.0.0.1:3030/Warcraft/update"
```

### Development

Made by [Michel Llorens](https://github.com/Michotastico) and [Tomas Saez](https://github.com/tsaezb).

License
----

GPL

[Jena]: <https://jena.apache.org>
[Fuseki]: <https://jena.apache.org/documentation/fuseki2>
[BeautifulSoup4]: <https://www.crummy.com/software/BeautifulSoup>
[SPARQLWrapper]: <https://rdflib.github.io/sparqlwrapper>
[Pycharm]: <https://www.jetbrains.com/pycharm>
[scraper]: <https://github.com/Michotastico/WarcraftRDF-Scraping>

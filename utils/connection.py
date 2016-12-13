#!/usr/bin/env python
# -*- coding: utf-8 -*-
from SPARQLWrapper import SPARQLWrapper, JSON


__author__ = "Michel Llorens"
__license__ = "GPL"
__version__ = "1.0.0"
__email__ = "mllorens@dcc.uchile.cl"

UPDATE_URL = "http://127.0.0.1:3030/Warcraft/update"
update_sparql = SPARQLWrapper(UPDATE_URL)

QUERY_URL = "http://127.0.0.1:3030/Warcraft/query"
query_sparql = SPARQLWrapper(QUERY_URL)


def update_sparql_server(data):
    """Send a update request."""
    update_sparql.resetQuery()
    update_sparql.method = 'POST'
    update_sparql.setQuery(data)
    update_sparql.query()


def query_sparql_server(query):
    """Send a query request and return a JSON result."""
    query_sparql.resetQuery()
    query_sparql.setQuery(query)
    query_sparql.setReturnFormat(JSON)
    results = query_sparql.query().convert()
    return results

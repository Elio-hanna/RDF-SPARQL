from rdflib import Graph, URIRef
from rdflib.namespace import RDFS, SKOS

g = Graph()
g.parse('../data/car-beuty.xml', format='xml')

qres = g.query('''
    SELECT ?sub ?pred ?label
    WHERE {
        ?sub ?pred ?label .
    } LIMIT 100
''')
for label, description in qres:
    print(f'pred: {label} label: {description}')


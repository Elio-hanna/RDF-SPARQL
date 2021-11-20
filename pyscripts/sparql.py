from rdflib import Graph, URIRef
from rdflib.namespace import RDFS, SKOS

g = Graph()
g.parse('leagues.xml', format='xml')

qres = g.query('''
    SELECT ?pred ?label
    WHERE {
        <http://example.org/instances/2> ?pred ?label .
    }
''')
for label, description in qres:
    print(f'pred: {label} label: {description}')


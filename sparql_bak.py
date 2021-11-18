from rdflib import Graph, URIRef,query
from rdflib.namespace import RDFS, RDF,OWL,FOAF
from rdflib import Namespace


# g = Graph()
# g.parse('leagues.xml', format='xml')

# DBO = Namespace('http://example.org/props/')
# DBR = Namespace('http://example.org/instances/')
# print("here")
g = Graph()
g.parse('https://www.wikidata.org/wiki/Special:EntityData/Q2831.ttl')

qres = g.query('''SELECT ?label WHERE { wd:Q2831 skos:altLabel ?label . }''')
for label, *_ in qres:
    print(label.value, label.language)
    break

# print(g.value(DBR['4'], DBO['understatNotation'],None))
# print(g.value(DBR['20317'], DBO['transmission'],None))



# from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF, CSV, TSV

# sparql = SPARQLWrapper("http://localhost/leagues.xml")
# sparql.setQuery("""
#     SELECT DISTINCT ?c
# WHERE {
#     <http://example.org/instances/3> <ns1:name> ?c .
# } LIMIT 1
# """)

# print('\n\n*** XML Example')
# sparql.setReturnFormat(XML)
# results = sparql.query().convert()
# print(results.toxml())

# for result in results["results"]["bindings"]:
#     print(result["label"]["value"])



# Convert results to JSON format
# sparql.setReturnFormat(JSON)
# print("here")
# result = sparql.query().convert()
# print("here")
# # The return data contains "bindings" (a list of dictionaries)
# for hit in result["results"]["bindings"]:
#     # We want the "value" attribute of the "comment" field
#     print(hit["comment"]["value"])


# import rdflib
# g = rdflib.Graph()
# g.parse('leagues.xml', format='xml')
# print("here")
# knows_query = """
# SELECT DISTINCT ?sujet ?objet
# WHERE {
#     ?sujet ?predicate ?objet .
# }"""
# print("here2")
# print(g)
# qres = g.query(knows_query)
# print("here3")
# for row in qres:
#     print(f"{row.aname} knows {row.bname}")






#get the predicate and print them to check if the code works
# properties1 = set()
# for p in g.predicates():
#     properties1.add(p)
# from pprint import pprint
# pprint(properties1)


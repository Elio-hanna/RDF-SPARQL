# from rdflib import Graph, URIRef
# from rdflib.namespace import RDFS, RDF,OWL,FOAF
# from rdflib import Namespace


# g = Graph()
# g.parse('car-beuty.xml', format='xml')

# DBO = Namespace('http://example.org/props/')
# DBR = Namespace('http://example.org/instances/')

# print(g.value(DBR['20317'], DBO['make'],None))
# print(g.value(DBR['20317'], DBO['transmission'],None))


from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF, CSV, TSV

sparql = SPARQLWrapper("http://danbri.org/foaf.rdf#")
sparql.setQuery("""
    SELECT DISTINCT ?aname ?bname
WHERE {
    ?a foaf:knows ?b .
    ?a foaf:name ?aname .
    ?b foaf:name ?bname .
}
""")

# JSON example
print('\n\n*** JSON Example')
sparql.setReturnFormat(JSON)
results = sparql.query().convert()
for result in results["results"]["bindings"]:
    print(result["label"]["value"])




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


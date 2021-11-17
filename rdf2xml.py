import rdflib

g=rdflib.Graph ()
g.load('./leagues.rdf',format='n3')
bs_data = g.serialize()
data = str(bs_data)
with open('./leagues.xml','w') as f:
    f.write(data)
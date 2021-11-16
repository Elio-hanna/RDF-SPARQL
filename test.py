import rdflib

g=rdflib.Graph ()
g.load('./car.rdf',format='n3')
bs_data = g.serialize()
data = str(bs_data)
with open('./car.xml','w') as f:
    f.write(data)
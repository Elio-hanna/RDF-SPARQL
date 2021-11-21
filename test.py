import re

query = "SELECT ?suj ?pred ?label WHERE { ?suj ?pred ?label .}"

query = list(query.split(" "))
result = set()
for i in query:
    if (i.startswith("?")):
        result.add(i)

print(list(result))
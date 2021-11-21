class QuerySplitting:
    def splitting(query):
        query = list(query.split(" "))
        result = set()
        for i in query:
            if (i.startswith("?")):
                result.add(i.replace("?",""))
        return result
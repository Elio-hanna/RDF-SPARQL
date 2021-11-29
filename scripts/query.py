from scripts.querysplitting import QuerySplitting
class Query:
    def query(g,sub,pred,obj):
        # if (pred != None and obj != None):
        #     query = "SELECT ?subject WHERE { ?subject " + pred + " " + obj + " .}"
        #     row = g.query(query)
        #     final_result = list(row)
        #     result_query = QuerySplitting.splitting(query)
        #     final_result.insert(0,list(result_query))

        if (sub != None and pred != None):
            query = "SELECT ?object WHERE { " + sub + " "+ pred + " ?object .}"
            row = g.query(query)
            final_result = list(row)
            result_query = QuerySplitting.splitting(query)
            final_result.insert(0,list(result_query))
            
        # if (sub != None and obj != None):
        #     print(sub,obj)
        #     query = "SELECT ?predicate WHERE { " + sub + " ?predicate "+ obj + " .}"
        #     row = g.query(query)
        #     final_result = list(row)
        #     result_query = QuerySplitting.splitting(query)
        #     final_result.insert(0,list(result_query))

        return final_result

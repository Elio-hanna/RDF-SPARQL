from scripts.querysplitting import QuerySplitting
class Query:
    def query(g,sub,pred,obj):
        if (sub != None and pred != None):
            query = "SELECT ?object WHERE { " + sub + " "+ pred + " ?object .}"
            row = g.query(query)
            final_result = list(row)
            result_query = QuerySplitting.splitting(query)
            final_result.insert(0,list(result_query))
        return final_result

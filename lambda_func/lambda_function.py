import constants as c
import snippets
import json
import search

def lambda_handler(event, context):

    body = event[c.REQUEST_BODY]
    data = json.loads(body)
    query = data[c.REQUEST_QUERY]
    
    if query[0] == c.LITERAL_SEARCH_SYMBOL:
        result = search.literal_search(query[1:])
    else:
        result = search.complex_search(query)
    
    response = snippets.response200
    response[c.REQUEST_BODY] = json.dumps(result, indent=2, ensure_ascii=False)
    
    return response
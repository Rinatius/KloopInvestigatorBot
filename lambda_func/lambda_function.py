import constants as c
import snippets
import json
import search
from user import User
import sheets

def lambda_handler(event, context):

    body = event[c.REQUEST_BODY]
    data = json.loads(body)
    query = data[c.REQUEST_QUERY]
    user_id = data[c.REQUEST_USER]
    
    user = User(user_id)
    
    print(event)
    
    result = search.search(query, user)
    
    if user.status[c.USER_INTEGRATIONS][c.INTEGRATIONS_SHEETS]==c.INTEGRATION_STATUS_READY and not result.empty:
        sheets.write(result, user)
    
    
    response = snippets.response200
    response[c.RESPONSE_BODY] = {}
    response[c.RESPONSE_BODY][c.RESPONSE_INFO] = json.dumps(result, indent=2, ensure_ascii=False)
    response[c.RESPONSE_BODY][c.RESPONSE_SERVICE_MESSAGES] = user.service_messages
    
    user.update()
    
    return response
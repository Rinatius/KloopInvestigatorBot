import requests
import connection

def dialogflow_request(query):
    user_session = "100500"
    url = 'https://api.dialogflow.com/v1/query/' 

    post_fields = {
      "v": "20170712",
      "query": [
        query
      ],
      "lang": "ru",
      "sessionId": user_session,
      "timezone": "Asia/Dhaka"
    }
    
    dialogflow_auth = 'Bearer ' + connection.DIALOGFLOW_AUTH

    headers = {'Authorization' : dialogflow_auth,
               'content-type' : 'application/json;charset=UTF-8'}

    response = requests.post(url, json=post_fields, headers=headers)
    return response.json()

def prepare_for_dialogflow(query):
    return query
    
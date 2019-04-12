import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import connection
import constants as c
from present import df_to_text

# Use a service account
cred = credentials.Certificate(c.FIREBASE_SERVICE_ACCOUNT_JSON)
firebase_admin.initialize_app(cred)

db = firestore.client()

def load_user_status(user_id):
    
    doc_ref = db.collection(c.DB_USERS_FIELD).document(user_id)
    user_status = None
    
    user_status = doc_ref.get().to_dict()
    
    if not user_status:
        user_status = c.DEFAULT_USER_STATUS
        #doc_ref.set(user_status)
        
    return user_status

def update_user_status(user_id, status):    
    doc_ref = db.collection(c.DB_USERS_FIELD).document(user_id)#.collection("properties").document("status")
    doc_ref.set(status)


def message_to_hook(user, message=None):

    if message is None:
        message = {'result': df_to_text(user.current_result), 'service_messages': user.service_messages}

    response = requests.post(connection.FLOWXO_HOOK['url'],
                             json={'full_response_path': connection.FLOWXO_HOOK['response_path'] + user.id,
                                   'key': connection.FLOWXO_HOOK['key'], 'data': message})

    print('----------Response from outgoing---------------')
    print(response)

    return response

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import constants as c

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
        doc_ref.set(user_status)
        
    return user_status

def update_user_status(user_id, status):    
    doc_ref = db.collection(c.DB_USERS_FIELD).document(user_id)#.collection("properties").document("status")
    doc_ref.set(status)
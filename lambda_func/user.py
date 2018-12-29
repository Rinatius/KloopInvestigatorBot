import adapter

class User:
    
    def __init__(self, user_id):
        self.id = user_id
        self.status = adapter.load_user_status(user_id)
        self.service_messages = ""
        
    def update(self):
        adapter.update_user_status(self.id, self.status)
import adapter

def message(user, message=None):
    adapter.message_to_hook(user, message)

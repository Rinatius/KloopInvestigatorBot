import os

DB = {'host': os.environ['INVBOT_DB_HOST'],
      'port': int(os.environ['INVBOT_DB_PORT']),
      'user': os.environ['INVBOT_DB_USER'],
      'passwd': os.environ['INVBOT_DB_PASSWD'],
      'db': os.environ['INVBOT_DB_NAME'],
      'charset': os.environ['INVBOT_DB_CHARSET']}

DIALOGFLOW_AUTH = os.environ['INVBOT_DIALOGFLOW_AUTH']

FLOWXO_HOOK = {'url': os.environ['INVBOT_FLOWXO_HOOK_URL'],
               'key': os.environ['INVBOT_FLOWXO_HOOK_KEY'],
               'response_path': os.environ['INVBOT_FLOWXO_HOOK_RESPONSE_PATH']}

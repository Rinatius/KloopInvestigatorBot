import os

DB = {'host' : os.environ['INVBOT_DB_HOST'],
      'port' : int(os.environ['INVBOT_DB_PORT']),
      'user' : os.environ['INVBOT_DB_USER'],
      'passwd' : os.environ['INVBOT_DB_PASSWD'],
      'db' : os.environ['INVBOT_DB_NAME'],
      'charset' : os.environ['INVBOT_DB_CHARSET']}

DIALOGFLOW_AUTH = os.environ['INVBOT_DIALOGFLOW_AUTH']
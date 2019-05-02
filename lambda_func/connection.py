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


# 'postgresql://scott:tiger@localhost/mydatabase'
DB_POSTGRESQL = 'postgresql:' \
                + '//' + os.environ['INVBOT_DB_USER'] \
                + ':' + os.environ['INVBOT_DB_PASSWD'] \
                + '@' + os.environ['INVBOT_DB_HOST'] \
                + ':' + os.environ['INVBOT_DB_PORT'] \
                + '/' + os.environ['INVBOT_DB_NAME']

# OTHER CONNECTIONS
# psycopg2
# ('postgresql+psycopg2://scott:tiger@localhost/mydatabase')

# pg8000
# ('postgresql+pg8000://scott:tiger@localhost/mydatabase')

# mysql
# ('mysql://scott:tiger@localhost/foo')

# mysqlclient (a maintained fork of MySQL-Python)
# ('mysql+mysqldb://scott:tiger@localhost/foo')

# PyMySQL
# 'mysql+pymysql://scott:tiger@localhost/foo')

# oracle
# 'oracle://scott:tiger@127.0.0.1:1521/sidname')

# oracle
# 'oracle+cx_oracle://scott:tiger@tnsname')

# pyodbc
# 'mssql+pyodbc://scott:tiger@mydsn')

# pymssql
# 'mssql+pymssql://scott:tiger@hostname:port/dbname')

# sqlite://<nohostname>/<path>
# where <path> is relative:
# 'sqlite:///foo.db')

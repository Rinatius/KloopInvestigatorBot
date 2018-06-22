echo off
ECHO Setting environment variables for InvestigativeBot test framework.
set INVBOT_DB_HOST=MYSQL_IP_ADDRESS
set INVBOT_DB_PORT=3306
set INVBOT_DB_USER=MYSQL_USER
set INVBOT_DB_PASSWD=MYSQL_PASSWORD
set INVBOT_DB_NAME=MYSQL_DB_NAME
set INVBOT_DB_CHARSET=utf8mb4
set INVBOT_DIALOGFLOW_AUTH=DIALOGFLOW_BEARER_AUTH_TOKEN
ECHO All variables set. You can start Jupyter Notebook now.
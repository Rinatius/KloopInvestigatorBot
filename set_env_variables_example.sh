#!/bin/bash

echo Setting environment variables for InvestigativeBot test framework.
export INVBOT_DB_HOST=""
export INVBOT_DB_PORT="3306"
export INVBOT_DB_USER=""
export INVBOT_DB_PASSWD=""
export INVBOT_DB_NAME=""
export INVBOT_DB_CHARSET="utf8mb4"
export INVBOT_DIALOGFLOW_AUTH=""
export INVBOT_FLOWXO_HOOK_URL=""
export INVBOT_FLOWXO_HOOK_KEY=""
export INVBOT_FLOWXO_HOOK_RESPONSE_PATH=""
echo All variables should have been set. You can start Jupyter Notebook now.
echo If variables are not set for the current session use source set_env_variables or . set_env_variables
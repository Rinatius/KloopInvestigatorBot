import pymysql
import pandas as pd
import json
from companysearcher import Companysearcher
import dialogflow_tools as dft
import queries
from queries import *
import service_functions
from service_functions import *
import snip
import connection
import present
import constants as c
import strings as s


def search(query, user):
    
    if query[0] == c.LITERAL_SEARCH_SYMBOL:
        literal_search(query[1:], user)
    elif query[0] == c.SERVICE_SYMBOL:
        service_function(query[1:], user)
    else:
        complex_search(query, user)


def service_function(query, user):
    #try:
    module = getattr(service_functions, query)
    module.serve(user)
    #except AttributeError:        
    #    user.service_messages.append({c.SERVICE_TEXTS: s.function_not_ready})
    
    
def literal_search(query, user):
    
    conn = pymysql.connect(**connection.DB)
    
    cs = Companysearcher(conn)
    df = cs.find(query)

    user.current_result = df
    user.current_query = query
    
    conn.close()


def complex_search(query, user):
    
    conn = pymysql.connect(**connection.DB)
    
    query_dialogflow = dft.prepare_for_dialogflow(query)
    response = dft.dialogflow_request(query_dialogflow)
    call_specific_search(query, response, conn, user)
    
    conn.close()


def call_specific_search(query, response, db_connection, user):
    try:
        module = getattr(queries, response["result"]["metadata"]["intentName"])
        df = module.search(db_connection, query, **response["result"]["parameters"])
        user.current_result = df
        user.current_query = query
    except AttributeError:
        user.update_service_messages(s.function_not_ready)

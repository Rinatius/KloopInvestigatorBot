import pymysql
import pandas as pd
import json
from companysearcher import Companysearcher
import dialogflow_tools as dft
import queries
from queries import *
import snippets
import connection

def literal_search(query):
    
    conn = pymysql.connect(**connection.DB)
    
    cs = Companysearcher(conn)
    companies = cs.find(query)
    
    conn.close()
    
    return companies

def complex_search(query):
    
    conn = pymysql.connect(**connection.DB)
    
    query_dialogflow = dft.prepare_for_dialogflow(query)
    response = dft.dialogflow_request(query_dialogflow)
    result = call_specific_search(query, response, conn)
    
    conn.close()
    
    return result

def call_specific_search(query, response, db_connection):
    try:
        module = getattr(queries, response["result"]["metadata"]["intentName"])
        dataframe = module.search(db_connection, query, **response["result"]["parameters"])
        result = snippets.df_to_dict(dataframe)
    except AttributeError:
        result = {"Sorry" : "Эта функция пока не доступна"}
    return result
    
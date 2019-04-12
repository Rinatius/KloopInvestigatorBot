import pandas as pd
import json

class Companysearcher:
    
    def __init__(self, db_connection):
        self.db_connection = db_connection
    
    def find(self, name):
        query = "SELECT FullNameRu, HeadName, Founders FROM Minjust2018 WHERE FullNameRu LIKE '%" + name + "%' LIMIT 0, 3"
        df = pd.read_sql_query(query, self.db_connection)
        return df

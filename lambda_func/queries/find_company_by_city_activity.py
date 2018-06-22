import pandas as pd

def search(db_connection, original_query, city, activity):
    df = pd.read_sql_query(
    "Select FullNameRu, Street, Building, Apartment, Founders From Minjust2018 where MainActivity like  '%" + activity[0]+ "%'AND City  like '%"+city[0]+"%' limit 0,10",
    db_connection)
    
    return df
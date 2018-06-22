import pandas as pd

def search(db_connection, original_query, street, building):
    df = pd.read_sql_query(
    "SELECT FullNameRu, Street, Building FROM Minjust2018 WHERE Street LIKE '%"+street[:-1]+"%' AND Building LIKE '"+building+"' LIMIT 0, 5",
    db_connection)
    return df
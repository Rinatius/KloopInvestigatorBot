import pandas as pd

def search(db_connection, original_query, name="", lastname=" ", patronymic=""):
    query = "SELECT fullName, fullAddress FROM persons WHERE fullName LIKE '%"+lastname[0]+" "+name[0]+" "+patronymic+"%' LIMIT 0, 20"
    print(query)
    df = pd.read_sql_query(query, db_connection)
    print(df)
    return df

 
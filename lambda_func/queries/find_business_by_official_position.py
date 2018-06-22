import pandas as pd

def search(db_connection, original_query, official_position):
    df = pd.read_sql_query(
    "SELECT declaration.last_name, declaration.first_name, declaration.middle_name, declaration.positn, Minjust2018.FullNameRu,Minjust2018.HeadName, Minjust2018.Founders FROM Minjust2018 JOIN declaration ON Minjust2018.Founders LIKE CONCAT('%', declaration.last_name, '%') AND Minjust2018.Founders LIKE CONCAT ('%', declaration.first_name, '%') WHERE declaration.positn LIKE ('%" +  official_position + "%') LIMIT 0, 20",
    db_connection)
    print(df)
    return df
import pandas as pd

def search(db_connection, original_query, products):
    df = pd.read_sql_query(
    "SELECT tender_num, org_name, purchase, plan_sum  FROM Tenders WHERE purchase LIKE ('%" + products + "%') LIMIT 0, 5",
    db_connection)
    return df
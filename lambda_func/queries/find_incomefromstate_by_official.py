import pandas as pd

def search(db_connection, original_query, lastname, name):
    df = pd.read_sql_query(
    "SELECT declaration.last_name, declaration.first_name, declaration.middle_name, declaration.positn, declaration.workplace, Budget2017.period, Budget2017.payer, Budget2017.details, Budget2017.sum FROM `Budget2017` JOIN `declaration` ON Budget2017.details LIKE CONCAT ('%', declaration.last_name, '%') AND Budget2017.details LIKE CONCAT ('%', declaration.first_name, '%') WHERE declaration.last_name LIKE ('%" + lastname + "%') AND declaration.first_name LIKE ('%" + name + "%') LIMIT 0, 10",
    db_connection)
    return df
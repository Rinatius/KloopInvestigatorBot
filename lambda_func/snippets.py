response200 = {"statusCode": 200, "headers": {"Content-Type": "application/json"}}

def df_to_dict(df):
    companies = {}
    companies_list = df.values.tolist()
    for company in companies_list:
        companies[company[0]] = company[-2:]            
    return companies
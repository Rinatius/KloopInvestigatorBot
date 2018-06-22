import pandas as pd

def search(db_connection, original_query, city, activity):
    print (activity)
    print (city)

    try:
        if city is None or  activity is None :
            df= pd.DataFrame(["Извините, деятельность или город не распознаны"])
        else:
            df = pd.read_sql_query("Select FullNameRu, Street, Building, Apartment, Founders, Url From Minjust2018 join Minjust2018_links on Minjust2018.links_id=Minjust2018_links.id where MainActivity like  '%" + activity[:-1]+ "%' and MainActivity IS NOT NULL AND City  like '%"+city[0]+"%' limit 0,10", db_connection)
        if df is None:
            df= pd.DataFrame(["Извините,запрос вернул пустой результат"])     
 
    except AttributeError:
        df= pd.DataFrame(["Попробуйте переформулировать"])     

    return df



    
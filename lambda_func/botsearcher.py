import pandas as pd
import sqlalchemy as db
import connection as con


class BotSearcher:

    def __init__(self):
        self.db_connection = con.DB_POSTGRESQL

    def find_company(self, table_name, company_name):
        '''
        query = "SELECT FullNameRu, HeadName, Founders FROM Minjust2018 WHERE FullNameRu LIKE '%" + name + "%' LIMIT 0, 3"
        df = pd.read_sql_query(query, self.db_connection)
        return df
        '''

        engine = db.create_engine(self.db_connection)
        connection = engine.connect()
        metadata = db.MetaData()
        table = db.Table(table_name, metadata, autoload=True, autoload_with=engine)

        query = db.select([table.columns.FullNameRu,
                           table.columns.HeadName,
                           table.columns.Founders]).where(table.columns.FullNameRu.like('%' + company_name + '%'))

        ResultProxy = connection.execute(query)

        ResultSet = ResultProxy.fetchall()
        df = pd.DataFrame(ResultSet[:3])

        return df

    def find_business_by_official_position(self, official_position):
        '''
        df = pd.read_sql_query(
            "SELECT declaration.last_name, declaration.first_name, declaration.middle_name, declaration.positn, Minjust2018.FullNameRu,Minjust2018.HeadName, Minjust2018.Founders FROM Minjust2018 JOIN declaration ON Minjust2018.Founders LIKE CONCAT('%', declaration.last_name, '%') AND Minjust2018.Founders LIKE CONCAT ('%', declaration.first_name, '%') WHERE declaration.positn LIKE ('%" + official_position + "%') LIMIT 0, 20",
            db_connection)
        print(df)
        return df
        '''

        engine = db.create_engine(self.db_connection)
        connection = engine.connect()
        metadata = db.MetaData()
        minjust2018 = db.Table('Minjust2018', metadata, autoload=True, autoload_with=engine)
        declaration = db.Table('declaration', metadata, autoload=True, autoload_with=engine)

        query = db.select([declaration.columns.last_name,
                           declaration.columns.first_name,
                           declaration.columns.middle_name,
                           declaration.columns.positn,
                           minjust2018.columns.FullNameRu,
                           minjust2018.columns.HeadName,
                           minjust2018.columns.Founders])

        query = query.select_from(minjust2018.join(declaration,
                                                   minjust2018.columns.Founders.like('%' + declaration.columns.last_name + '%') and
                                                   minjust2018.columns.Founders.like('%' + declaration.columns.first_name + '%'))).where(declaration.columns.positn.like('%' + official_position + '%'))

        ResultProxy = connection.execute(query)

        ResultSet = ResultProxy.fetchall()
        df = pd.DataFrame(ResultSet[:20])

        return df

    def find_companies_by_address(self, street, building):
        '''
        df = pd.read_sql_query(
            "SELECT FullNameRu, Street, Building FROM Minjust2018 WHERE Street LIKE '%"+street[:-1]+"%' AND Building LIKE '"+building+"' LIMIT 0, 5",
            db_connection)
        print(df)
        return df
        '''

        engine = db.create_engine(self.db_connection)
        connection = engine.connect()
        metadata = db.MetaData()
        table = db.Table('Minjust2018', metadata, autoload=True, autoload_with=engine)

        query = db.select([table.columns.FullNameRu,
                           table.columns.Street,
                           table.columns.Building]).where(
            table.columns.Street.like('%' + street[:-1] + '%') and table.columns.Building.like(
                '%' + building + '%'))

        ResultProxy = connection.execute(query)

        ResultSet = ResultProxy.fetchall()
        df = pd.DataFrame(ResultSet[:5])

        return df

    def find_company_by_city_activity(self, city, activity):
        '''
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
        '''

        try:
            if city is None or activity is None:
                df = pd.DataFrame(["Извините, деятельность или город не распознаны"])
            else:
                engine = db.create_engine(self.db_connection)
                connection = engine.connect()
                metadata = db.MetaData()
                minjust2018 = db.Table('Minjust2018', metadata, autoload=True, autoload_with=engine)
                minjust2018_links = db.Table('Minjust2018_links', metadata, autoload=True, autoload_with=engine)

                query = db.select([minjust2018.columns.FullNameRu,
                                   minjust2018.columns.Street,
                                   minjust2018.columns.Building,
                                   minjust2018.columns.Apartment,
                                   minjust2018.columns.Founders,
                                   minjust2018.columns.Url])

                query = query.select_from(minjust2018.join(minjust2018_links,
                                                           minjust2018.columns.Founders == minjust2018_links.columns.id)).where(
                                                    minjust2018.columns.MainActivity.like('%' + activity[:-1] + '%') and
                                                    minjust2018.columns.MainActivity != None and
                                                    minjust2018.columns.City.like('%' + city[0] + '%'))

                ResultProxy = connection.execute(query)

                ResultSet = ResultProxy.fetchall()
                df = pd.DataFrame(ResultSet[:10])
            if df is None:
                df = pd.DataFrame(["Извините,запрос вернул пустой результат"])

        except AttributeError:
            df = pd.DataFrame(["Попробуйте переформулировать"])

        return df

    def find_incomefromstate_by_official(self, lastname, name):
        '''
        "SELECT declaration.last_name, declaration.first_name, declaration.middle_name, declaration.positn, declaration.workplace, Budget2017.period, Budget2017.payer, Budget2017.details, Budget2017.sum FROM `Budget2017` JOIN `declaration` ON Budget2017.details LIKE CONCAT ('%', declaration.last_name, '%') AND Budget2017.details LIKE CONCAT ('%', declaration.first_name, '%') WHERE declaration.last_name LIKE ('%" + lastname + "%') AND declaration.first_name LIKE ('%" + name + "%') LIMIT 0, 10",
        '''

        engine = db.create_engine(self.db_connection)
        connection = engine.connect()
        metadata = db.MetaData()
        budget2017 = db.Table('Budget2017', metadata, autoload=True, autoload_with=engine)
        declaration = db.Table('declaration', metadata, autoload=True, autoload_with=engine)

        #` WHERE declaration.last_name LIKE ('%" + lastname + "%') AND declaration.first_name LIKE ('%" + name + "%') LIMIT 0, 10",
        query = db.select([declaration.columns.last_name,
                           declaration.columns.first_name,
                           declaration.columns.middle_name,
                           declaration.columns.positn,
                           declaration.columns.workplace,
                           budget2017.columns.period,
                           budget2017.columns.payer,
                           budget2017.columns.details,
                           budget2017.columns.sum])


        query = query.select_from(budget2017.join(declaration,
                                                  budget2017.columns.details.like('%' + declaration.columns.last_name + '%') and
                                                  budget2017.columns.details.like('%' + declaration.columns.first_name + '%'))).where(
            declaration.columns.last_name.like('%' + lastname + '%') and
            declaration.columns.first_name.like('%' + name + '%'))

        ResultProxy = connection.execute(query)

        ResultSet = ResultProxy.fetchall()
        df = pd.DataFrame(ResultSet[:10])

    def find_tenders_by_product(self, products):
        '''
        "SELECT tender_num, org_name, purchase, plan_sum  FROM Tenders WHERE purchase LIKE ('%" + products + "%') LIMIT 0, 5",
        '''

        engine = db.create_engine(self.db_connection)
        connection = engine.connect()
        metadata = db.MetaData()
        table = db.Table('Tenders', metadata, autoload=True, autoload_with=engine)

        query = db.select([table.columns.tender_num,
                           table.columns.org_name,
                           table.columns.purchase,
                           table.columns.plan_sum]).where(table.columns.purchase.like('%' + products + '%'))

        ResultProxy = connection.execute(query)

        ResultSet = ResultProxy.fetchall()
        df = pd.DataFrame(ResultSet[:5])

        return df

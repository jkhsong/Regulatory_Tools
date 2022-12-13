import source.rst_reader as rr
import source.connectors as ct
import pandas as pd


class RSTqueries():
    def __init__(self) -> None:
        rst_dfs = rr.read_xl('X:\\Dropbox\\GitHub\\Skeleton_DB\\datafiles\\', 'catalogofrsts.xlsx')
        self.data = rst_dfs.get_rsts()
    
    def input_RSTs(self, skeldb: ct.PostgresConnector):
        rst_data = self.data
        for i in range(len(rst_data)):
            Area, Type, Description = rst_data[i][1], rst_data[i][2], rst_data[i][0]
            skeldb.execute_command(f"INSERT INTO test (Area, Type, Description) VALUES (\'{Area}\', \'{Type}\', \'{Description}\')")
    
    def lookup_RST_table(self, skeldb: ct.PostgresConnector):
        skeldb.print_query_results("SELECT Area, Type FROM test;", [1,0])

    def lookup_area_crude(self, skeldb: ct.PostgresConnector):
        skeldb.print_query_results("""SELECT DISTINCT(Area)
                                      FROM test ORDER BY Area ASC""")

    def lookup_by_area(self, skeldb: ct.PostgresConnector):
        skeldb.print_query_results("""SELECT Area, Type 
                                      FROM test
                                      ORDER BY Area ASC, Type ASC;
                                        """)
    def lookup_by_area_counts(self, skeldb: ct.PostgresConnector):
        skeldb.print_query_results("""SELECT Area, TYPE, COUNT(Type) 
                                      FROM test
                                      GROUP BY Area, Type
                                      ORDER BY Area ASC, Type ASC;
                                        """)

    def lookup_by_type_counts(self, skeldb: ct.PostgresConnector):
        skeldb.print_query_results("""SELECT Type, Area, COUNT(Area) 
                                      FROM test
                                      GROUP BY Type, Area
                                      ORDER BY Type ASC, Area ASC;
                                        """)
    
    def lookup_distinct_RST(self, skeldb: ct.PostgresConnector):
        skeldb.print_query_results("""Select DISTINCT(Type) from test ORDER BY Type ASC""")
    
    def lookup_distinct_areas(self, skeldb: ct.PostgresConnector):
        skeldb.print_query_results("""Select DISTINCT(Area) from test ORDER BY Area ASC""")
    
    def query_root_areas(self, skeldb: ct.PostgresConnector):
        unique = []
        results = skeldb.query_all("""Select DISTINCT(Area) from test ORDER BY Area ASC""")
        for i,result in enumerate(results):
            proxyresults = results.copy()
            del proxyresults[i]
            check = any(result[0] in sub[0] for sub in proxyresults if len(result[0])<=len(sub[0]))
            if (check == True and result[0] not in unique): ## Reduce Area by root word
                unique.append(result[0])
        return unique
    
    def lookup_root_frequency(self, skeldb: ct.PostgresConnector):
        root_list = self.query_root_areas(skeldb)
        data = self.data
        category = {}
        for root in root_list:
            category[root] = 0
            for item in data:
                if root in item[1]:
                    category[root] += 1
        for item in category:
            print(f'{item}: {category[item]}')

    def lookup_area_breakdown(self, skeldb: ct.PostgresConnector):
        root_list = self.query_root_areas(skeldb)
        type_list = skeldb.query_all("""Select DISTINCT(Type) from test ORDER BY Type ASC""")
        data = self.data

        category = {}
        for root in root_list:
            category[root] = {}
            for type in type_list:
                typec = type[0]
                category[root][typec] = 0
                for item in data:
                    if root in item[1] and typec in item[2]:
                        category[root][typec] += 1
        # for item in category:
        #     print(f'{item}: {category[item]}')   
        dfcat = pd.DataFrame(category).transpose()
        print(dfcat)


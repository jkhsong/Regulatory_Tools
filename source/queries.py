import source.rst_reader as rr
import source.connectors as ct
import source.mlalgorithms as ml
from typing import Union
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt



class RSTqueries():
    def __init__(self) -> None:
        rst_dfs = rr.read_xl('X:\\Dropbox\\GitHub\\Skeleton_DB\\datafiles\\', 'catalogofrsts.xlsx')
        self.data = rst_dfs.get_rsts()
    
    def input_RSTs(self, skeldb: Union[ct.PostgresConnector, ct.MongoConnector]):
        rst_data = self.data
        for i in range(len(rst_data)):
            Area, Type, Description = rst_data[i][1], rst_data[i][2], rst_data[i][0]
            skeldb.execute_command(f"INSERT INTO test (Area, Type, Description) VALUES (\'{Area}\', \'{Type}\', \'{Description}\')")
    
    def lookup_RST_table(self, skeldb: ct.PostgresConnector):
        skeldb.print_query_results("SELECT Area, Type FROM test;", [1,0])

    def lookup_RST_counts(self, skeldb: ct.PostgresConnector):
        printback = skeldb.query_all("SELECT Type, COUNT(Type) from test GROUP BY Type ORDER BY Type ASC;")
        printback_dict = {}
        for i,item in enumerate(printback):
            printback_dict[item[0]] = {'Counts': printback[i][1]}
        dfcat = pd.DataFrame(printback_dict)
        dfcat = dfcat.transpose()
        print(dfcat.to_markdown())

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
        return skeldb.query_all("""Select DISTINCT(Type) from test ORDER BY Type ASC""")
    
    def lookup_distinct_areas(self, skeldb: ct.PostgresConnector):
        skeldb.print_query_results("""Select DISTINCT(Area) from test ORDER BY Area ASC""")

    def lookup_distinct_areas_by_count(self, skeldb: ct.PostgresConnector):
        query = skeldb.query_all("""Select Area from test ORDER BY Area ASC""")
        roots = self.query_root_areas(skeldb)
        rootdict = {}
        for item in roots:
            rootdict[item] = 0
            for area in query:
                if item in area[0]:
                    rootdict[item] += 1
        final_list = {}
        for item in rootdict:
            final_list[item] = {'#': rootdict[item]}
        dfcat = pd.DataFrame.from_dict(final_list)
        dfcat = dfcat.transpose()
        print(dfcat.to_markdown())

    
    def query_root_areas(self, skeldb: ct.PostgresConnector):
        unique = []
        results = skeldb.query_all("""Select DISTINCT(Area) from test ORDER BY Area ASC""")
        for i,result in enumerate(results):
            proxyresults = results.copy()
            del proxyresults[i]
            check = any(result[0] in sub[0] for sub in proxyresults if len(result[0])<=len(sub[0]))
            if (check == True and result[0] not in unique): ## Reduce Area by root word
                unique.append(result[0])
            if (check == False and any([item in result[0] for item in unique])==False):
                unique.append(result[0])
        return unique
    
    def lookup_root_frequency_by_rst(self, skeldb: ct.PostgresConnector):
        root_list = self.query_root_areas(skeldb)
        data = self.data
        category = {}
        for root in root_list:
            category[root] = 0
            for item in data:
                if root in item[1]:
                    category[root] += 1
        rootdict = {}
        for item in category:
            rootdict[item] = {'#RSTs Available': category[item]}
        dfcat = pd.DataFrame(rootdict)
        dfcat = dfcat.transpose()
        print(dfcat.to_markdown())

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
        print(dfcat.to_markdown())
        return dfcat
    
    def lookup_kmeans_areas(self, skeldb: ct.PostgresConnector):
        dfcat = self.lookup_area_breakdown(skeldb)
        dfcat = dfcat.transpose()
        dfdict = dfcat.to_dict()
        area_matrix, area_dict = [], {}
        for area in dfdict:
            sublist = []
            for type in dfdict[area]:
                sublist.append(dfdict[area][type])
            area_matrix.append(sublist)
            area_dict[area] = sublist
        
        inertias = []
        ##Finding elbow
        # for i in range(1,len(area_matrix)):
        #     p = ml.kmeans(area_matrix,k=i)
        #     array,inertia = p.classify()
        #     inertias.append(inertia)    
        # fig = plt.figure(figsize=(15, 5))
        # plt.plot(range(1, len(area_matrix)), inertias)
        # plt.grid(True)
        # plt.title('Elbow curve')
        # plt.show()
        p = ml.kmeans(area_matrix,k=4)
        array,inertia = p.classify()

        idx = tuple([item for item in area_dict]) ##areas list
        tuplelist = tuple([tuple(i) for i in area_matrix])
        
        arrays = [array, idx, tuplelist]

        dfcat = pd.DataFrame(arrays).transpose()
        dfcat.columns = ['Category','Area of Research','RSTs (C, D, L, M, MD, PP, PV)']
        dfcat = dfcat.sort_values(by=['Category']).set_index('Area of Research')
        print(dfcat.to_markdown())

    def lookup_kmeans_areas_normalized(self, skeldb: ct.PostgresConnector):
            dfcat = self.lookup_area_breakdown(skeldb)
            dfcat = dfcat.transpose()
            dfdict = dfcat.to_dict()
            area_matrix, area_dict = [], {}
            for area in dfdict:
                sublist = []
                total = sum([dfdict[area][type] for type in dfdict[area]])
                for type in dfdict[area]:
                    sublist.append(dfdict[area][type]/total)
                area_matrix.append(sublist)
                area_dict[area] = sublist
            
            inertias = []
            ## Finding elbow
            # for i in range(1,len(area_matrix)):
            #     p = ml.kmeans(area_matrix,k=i)
            #     array,inertia = p.classify()
            #     inertias.append(inertia)    

            # fig = plt.figure(figsize=(15, 5))
            # plt.plot(range(1, len(area_matrix)), inertias)
            # plt.grid(True)
            # plt.title('Elbow curve')
            # plt.show()

            p = ml.kmeans(area_matrix,k=4)
            array,inertia = p.classify()

            idx = tuple([item for item in area_dict]) ##areas list

            tuplelist = np.round(area_matrix, 2)     
            tuplelist = tuple([tuple(i) for i in tuplelist])
            
            arrays = [array, idx, tuplelist]

            dfcat = pd.DataFrame(arrays).transpose()
            dfcat.columns = ['Category','Area of Research','RSTs (C, D, L, M, MD, PP, PV)']
            dfcat = dfcat.sort_values(by=['Category']).set_index('Area of Research')
            print(dfcat.to_markdown())  


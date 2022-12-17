import source.connectors as ct
import source.rst_reader as rr
import source.queries as queries

user = ct.User()
user.username = 'postgres'
user.password = 'testdb'
dbname = 'postgres'
skeldb = ct.PostgresConnector(user, dbname, None, None)

skeldb.open_connection()
skeldb.execute_command("CREATE TABLE test (Area varchar, Type varchar, Description varchar PRIMARY KEY);")
RST_lookup = queries.RSTqueries()

##Main menu
print('Welcome to the RST table explorer.')
RST_lookup.input_RSTs(skeldb)
print('**Successfully input data from the RSTs xlsx into PostgreSQL**')
print('Input your choice below:')
print('1: Return RST table (i.e. Type, Area of Research, Description, etc.')
print('2: Metrics by RST type (i.e. Phantom, Model, Dataset, etc.')
print('3: Metrics by Area of Research (i.e. Cardiovascular, Medical Imaging, etc.)')
# choice = int(input(f'Pick 1-3: '))

# if choice == 1:
#     RST_lookup.lookup_RST_table(skeldb)

# RST_lookup.lookup_RST_counts(skeldb)  ##Lookup RST counts


# RST_lookup.lookup_by_type_counts(skeldb)  ##Lookup RST broken down by count

# RST_lookup.lookup_distinct_areas(skeldb)

# RST_lookup.lookup_distinct_areas_by_count(skeldb)

# print(*RST_lookup.query_root_areas(skeldb), sep='\n')

# RST_lookup.lookup_root_frequency_by_rst(skeldb)

# RST_lookup.lookup_area_breakdown(skeldb)

# RST_lookup.lookup_kmeans_areas(skeldb)

RST_lookup.lookup_kmeans_areas_normalized(skeldb)



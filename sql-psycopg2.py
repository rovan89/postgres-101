import psycopg2

# connect to "chinook" datdbase
connection = psycopg2.connect(database="chinook")

# build a cursor object of the data
cursor = connection.cursor()

# Query 1 - select all records from the "Artist" table
cursor.execute('SELECT * FROM "Artist"')

# fetch the results (multiple)
results = cursor.fetchall()

# fetch the result (single)
#results = cursor.fetchone()

# closse the connection
connection.close()

# print results
for result in results:
    print(result)
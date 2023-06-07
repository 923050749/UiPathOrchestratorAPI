import cx_Oracle

# Set up the connection details
dsn = cx_Oracle.makedsn(host='localhost', port=1521, sid='your_sid')
username = 'your_username'
password = 'your_password'

# Establish the connection
connection = cx_Oracle.connect(username, password, dsn)

# Create a cursor to execute SQL statements
cursor = connection.cursor()

# Execute a SQL query
sql_query = 'SELECT * FROM your_table'
cursor.execute(sql_query)

# Fetch and print the results
for row in cursor:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()

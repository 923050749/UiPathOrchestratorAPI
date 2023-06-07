import cx_Oracle
import pandas as pd

# Set up the connection details
dsn = cx_Oracle.makedsn(host='localhost', port=1521, sid='your_sid')
username = 'your_username'
password = 'your_password'

# Establish the connection
connection = cx_Oracle.connect(username, password, dsn)

# Create a cursor to execute SQL statements
cursor = connection.cursor()

# Execute the SQL query
sql_query = 'SELECT * FROM your_table'
cursor.execute(sql_query)

# Get the column names
columns = [desc[0] for desc in cursor.description]

# Check if the Excel file exists
excel_file = 'output.xlsx'
try:
    # If the file exists, load the existing data into a DataFrame
    df = pd.read_excel(excel_file)
    # Append the new data to the DataFrame
    df_new = pd.DataFrame(cursor.fetchall(), columns=columns)
    df = df.append(df_new, ignore_index=True)
except FileNotFoundError:
    # If the file doesn't exist, create a new DataFrame with headers
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=columns)

# Save the DataFrame to an Excel file
df.to_excel(excel_file, index=False)

# Close the cursor and connection
cursor.close()
connection.close()

print(f"Table data saved to '{excel_file}' successfully.")

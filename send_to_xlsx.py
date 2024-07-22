import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('merrjep.db') 

# Write the SQL query to select specific columns
query = """Select * FROM Listings"""

# Use pandas to read the data into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Specify the Excel file name
excel_file = 'merrjep.xlsx'

# Write the DataFrame to an Excel file
df.to_excel(excel_file, index=False)

print(f"Data successfully written to {excel_file}")
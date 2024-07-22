import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('merrjep.db') 

# Write the SQL query to select specific columns
query = """
SELECT Date, Surface, Price FROM Listings 
WHERE Type = 'Shitet' AND Currency = 'EUR' AND 
Price > 4000 AND Price < 2000000 AND
Surface > 45 AND Surface < 999
Group by Surface, Price 
ORDER BY Date
"""

# Use pandas to read the data into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Display the first few rows of the DataFrame
print(df.head())

# Convert the Date column to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')

# Create a new column for Price per square meter
df['Pricepersqm'] = df['Price'] / df['Surface']

# Group data by month and calculate average Price per square meter
df['Month'] = df['Date'].dt.to_period('M')
monthly_avg = df.groupby('Month')['Pricepersqm'].mean().reset_index()

# Convert Period to datetime for plotting
monthly_avg['Month'] = monthly_avg['Month'].dt.to_timestamp()

# Plot the results
plt.figure(figsize=(12, 8))
plt.plot(monthly_avg['Month'], monthly_avg['Pricepersqm'], marker='o', linestyle='-', color='purple')

# Adding title and labels
plt.title('Average Price per Square Meter by Month')
plt.xlabel('Month')
plt.ylabel('Average Price per Square Meter (EUR)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid()

plt.savefig('price_trends.png')
plt.show()


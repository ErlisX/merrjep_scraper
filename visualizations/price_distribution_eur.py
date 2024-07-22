import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to db
conn = sqlite3.connect('merrjep.db')

# SQL query
query = "SELECT Link, Price FROM Listings WHERE Type = 'Shitet' and Currency = 'EUR' and Price > 4000 and Surface > 45 and Price < 2000000 and Surface < 999 Group by Surface, Price ORDER BY Price" 

# Read to df
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Display the first few rows of the DataFrame
print(df.head())

# Create bar chart.
bins = [0, 120000, 200000, 500000]
labels = ['0-120000', '120000-200000', '200000-500000']

# Cut the Price column into the defined bins
df['Price'] = pd.cut(df['Price'], bins=bins, labels=labels, include_lowest=True)

# Count the number of entries in each bucket
bucket_counts = df['Price'].value_counts().sort_index()

# Plot the bar chart
bucket_counts.plot(kind='bar', color='purple', alpha=0.7)

# Adding title and labels
plt.title('Number of Listings in Each Price Range')
plt.xlabel('Price per Range (EUR)')
plt.ylabel('Number of Listings')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
# Annotate each bar with the count
for index, value in enumerate(bucket_counts):
    plt.text(index, value, str(value), ha='center', va='bottom', fontsize=12)

plt.savefig('price_distribution.png')
plt.show()
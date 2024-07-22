import json
import csv
from pathlib import Path
import sqlite3
from datetime import datetime

# Send to sqlite3
con = sqlite3.connect('merrjep.db')
cur = con.cursor()

# Define the path to the JSON file
input_path = Path('transformed_njoftime.json')
output_path = Path('standardized_njoftime.json')

# Load the JSON data into python object (list).
data = json.loads(input_path.read_text(encoding='utf-8'))

# Extract only specific data from each posting.
extracted_chars = [
        'Link',
        'Data e Publikimit',
        'Cmimi',
        'Valuta',
        'Adresa/Rruga:',
        'Siperfaqe:',
        'Lloji i njoftimit:',
        'Komuna:',
]

extracted_posts = []
for d in data:
    extracted_post = {}
    for key in extracted_chars:
        if key in d.keys():
            extracted_post[key] = d[key]
        else:
            extracted_post[key] = None

    extracted_posts.append(extracted_post)

# Clean column Siperfaqe:
for d in extracted_posts:
    try:
        d['Siperfaqe:'] = d['Siperfaqe:'][:-3]
    except TypeError:
        continue


# Extract all values as list of lists.
values = []
for d in extracted_posts:
    values.append(list(d.values()))
    
# Create and fill sql table
cur.execute('''CREATE TABLE IF NOT EXISTS Listings
                    (Link text PRIMARY KEY, Date text, Price real, Currency text, Address text, Surface text, Type text, Location text)''')

cur.executemany("INSERT OR IGNORE INTO Listings VALUES (?, ?, ?, ?, ?, ?, ?, ?)", values)
con.commit()

# Close the cursor and connection
cur.close()
con.close()

import sqlite3

con = sqlite3.connect('merrjep.db')
cur = con.cursor()

month_map = {
    "Jan": "01", "Shk": "02", "Mar": "03", "Pri": "04",
    "Maj": "05", "Qer": "06", "Korr": "07", "Gush": "08",
    "Sht": "09", "Tet": "10", "Nen": "11", "Dhj": "12"
}

def convert_date_str(date_str):
    month, day, year = date_str.split('-')
    month = month_map[month]
    day = day.zfill(2) 
    return f"{day}-{month}-{year}"

# Fetch the rows with dates
cur.execute("SELECT Link, Date FROM Listings")
rows = cur.fetchall()


# Update the rows with the new date format
for row in rows:
    link, date = row
    print(date)
    old_date = date
    new_date_str = convert_date_str(old_date)
    cur.execute("UPDATE Listings SET Date = ? WHERE Link = ?", (new_date_str, link))

# Commit the changes
con.commit()

# Close the cursor and connection
cur.close()
con.close()
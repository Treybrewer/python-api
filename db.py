import sqlite3
from sqlite3 import Error
import csv
import pandas as pd

def convert_file_to_csv():
    cols = ["area", "perimter", "compactness", "length", "width", "asymmetry", "groove", "item_class"]
    df = pd.read_csv("seeds_dataset.txt", names=cols, sep="\s+")
    df.to_csv("seeds_dataset.csv", index=False)

def upload_csv():
    # Connect to SQLite database
    conn = sqlite3.connect('pythonsqlite.db')
    c = conn.cursor()

    # Create table to store CSV data
    c.execute('''CREATE TABLE IF NOT EXISTS seeds_dataset
                 (area, perimter, compactness, length, width, asymmetry, groove, item_class)''')

    # Open CSV file and insert data into table
    with open('seeds_dataset.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            c.execute('INSERT INTO seeds_dataset VALUES (?, ?, ?, ?, ?, ?, ?, ?)', row)

    # Commit changes and close connection
    conn.commit()
    conn.close()



if __name__ == '__main__':
    convert_file_to_csv()
    upload_csv()

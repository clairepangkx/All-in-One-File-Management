import sqlite3
import csv

def DB_exporter():
    conn = sqlite3.connect('AllinOne.db')
    c = conn.cursor()
    c.execute("SELECT * FROM files WHERE deleted = 'N' ORDER BY modification DESC")
    rows = c.fetchall()

    csv_name = 'AllinOne_reader.csv'
    with open(csv_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['ID', 'File Type', 'Name', 'Note', 'Modification Date', 'Creation Date', 'Path', 'Deleted'])
        csv_writer.writerows(rows)

    conn.close()

DB_exporter()

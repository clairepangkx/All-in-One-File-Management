import sqlite3 as sql
from pathlib import Path
from datetime import datetime
from utils.extensions import extension_paths

conn = sql.connect('AllinOne.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS files
        (id INTEGER PRIMARY KEY, file_type TEXT, name TEXT,
        note TEXT, modification TEXT, creation TEXT, 
        path TEXT UNIQUE, deleted TEXT DEFAULT 'N')''')

def upsert_file_info(file_type, name, creation_date, modification_date, path):
    formatted_modification_date = modification_date.strftime("%b/%d/%Y")
    #check if file is already in database
    c.execute('SELECT modification FROM files WHERE path = ?', (path,))
    recorded_version_date = c.fetchone()

    if recorded_version_date:
        #if file is seen before, check if the modification date has changed
        if recorded_version_date[0] != formatted_modification_date:
            #if there has been modifications, update modification date
            #NO VERSION TRACKING!
            c.execute('''UPDATE files SET modification = ?, WHERE path = ?''', 
                      (formatted_modification_date, path))
    else: #if the file has not been added to db before, insert new record of all data
        formatted_creation_date = creation_date.strftime("%b/%d/%Y")
        c.execute('''INSERT INTO files (file_type, name, creation, modification, path)
                    VALUES (?, ?, ?, ?, ?)''', (file_type, name, formatted_creation_date, formatted_modification_date, path))
    
    c.execute("UPDATE files SET deleted = 'N' WHERE path = ?", (path,))
    conn.commit()

def scan_and_upsert(watch_path):
    # First mark all files as deleted then unmark as we visit them.
    c.execute("UPDATE files SET deleted = 'Y'")
    for item in watch_path.rglob('*'):
        if item.is_file() and not (item.name.startswith('~') or item.name.startswith('.')):
            file_extension = item.suffix.lower()
            if file_extension == '':
                file_type = 'unknown'
            else:
                try:
                    file_type = extension_paths[file_extension]
                except KeyError:
                    file_type = 'unknown'
            name = item.name
            creation_date = datetime.fromtimestamp(item.stat().st_ctime)
            modification_date = datetime.fromtimestamp(item.stat().st_mtime)
            path = str(item)

            upsert_file_info(file_type, name, creation_date, modification_date, path)

watch_path = Path.home() / 'Desktop' / 'AllinOne'
scan_and_upsert(watch_path)

conn.close()
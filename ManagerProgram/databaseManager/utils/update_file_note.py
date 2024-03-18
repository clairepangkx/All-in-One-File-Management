import sqlite3

def update_file_note(file_id, note_text, override=False):
    conn = sqlite3.connect('AllinOne.db')
    c = conn.cursor()
    
    c.execute("SELECT deleted FROM files WHERE id = ?", (file_id,))
    req_result = c.fetchone()
    if req_result:
        if req_result[0] == 'Y':
            print(f"This file with ID {file_id} has been deleted")
            return
    else:
        print(f"No file found with ID {file_id}.")
        return


    if override:
        c.execute("UPDATE files SET note = ? WHERE id = ?", (note_text, file_id))
        conn.commit()
        c.execute("SELECT name FROM files WHERE id = ?", (file_id,))
        result = c.fetchone()
        print(f"Successfully overridden note for file {result[0]} with ID {file_id}")

    else:
        # Retrieve the current note for the file
        c.execute("SELECT note, name FROM files WHERE id = ?", (file_id,))
        result = c.fetchone()
        
        # Concatenate the new note to the existing note with 2 newlines
        current_note = result[0] if result[0] else ""  # Handle the case where the current note might be None
        updated_note = current_note + "\n\n" + note_text if result[0] else note_text
        c.execute("UPDATE files SET note = ? WHERE id = ?", (updated_note, file_id))
        conn.commit()
        print(f"Successfully added note for file {result[1]}, file ID {file_id}")

    conn.close()


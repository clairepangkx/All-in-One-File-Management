from utils.update_file_note import update_file_note

file_id = 6
note_text = "test note"
override_existing = False

update_file_note(file_id,note_text, override=override_existing)

# #uncomment the following to show in readable csv
# from DB_exporter import DB_exporter
# DB_exporter()
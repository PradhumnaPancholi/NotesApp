from Models.Note import Note

print("Welcome, Let's start taking notes !!! \n")

# to take user input for note
note_title = input("Enter a title for your note : ")
note_body = input("Enter your data : ")

new_note = Note(note_title, note_body)
new_note.create_note()
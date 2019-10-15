class Note:

    def __init__(self, title, body):
        self.title = title
        self.body = body

    # method to create a note
    def create_note(self):
        # to take user input for note
        note_title = input("Enter a title for your note : ")
        note_body = input("Enter your data")

        # to create a file and write data for user note
        note_file = open(note_title, "w")
        note_title.write(note_body)

        print("\n Congratulations, note saved")

class Note:

    def __init__(self, title, body):
        self.title = title
        self.body = body

    # method to create a note
    def create_note(self):
        # to create a file and write data for user note
        note_file = open(self.title, "w")
        note_file.write(self.body)

        print("\n Congratulations, note saved")

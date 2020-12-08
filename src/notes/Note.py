class Note:
    def __init__(self, name, note):
        if type(name) != str:
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name cannot be an empty string")
        if type(note) != float:
            raise TypeError("Note must be a float type")
        if not 2 < note < 6:
            raise ValueError("Note must be in beteween 2 and 6")
        self.name = name
        self.note = note

    def get_name(self):
        return self.name

    def get_note(self):
        return self.note


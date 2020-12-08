from .NoteStorage import NoteStorage


class NoteService:
    def __init__(self):
        self.note_storage = NoteStorage()

    def add(self, note):
        return self.note_storage.add(note)

    def average_of(self, name):
        if type(name) != str:
            raise TypeError("Name must be a string")
        all_notes = list(map(lambda note: note.get_note(), self.note_storage.get_all_notes_of(name)))
        num_of_notes = len(all_notes)
        if num_of_notes == 0:
            raise ValueError("No notes found")
        return sum(all_notes) / num_of_notes

    def clear(self):
        return self.note_storage.clear()

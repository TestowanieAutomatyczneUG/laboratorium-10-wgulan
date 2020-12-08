import unittest
from unittest.mock import *
from src.notes.Note import Note
from src.notes.NoteStorage import NoteStorage
from src.notes.NoteService import NoteService


class TestNoteService(unittest.TestCase):

    @patch.object(NoteStorage, 'add')
    def test_note_service_add(self, mock_method):
        mock_method.return_value = True
        test_service = NoteService()
        self.assertEqual(test_service.add(Note("John", 4.0)), True)

    @patch.object(NoteStorage, 'get_all_notes_of')
    def test_note_service_average_of(self, mock_method):
        mock_method.return_value = [Note("John", 4.0), Note("John", 3.5)]
        test_service = NoteService()
        self.assertEqual(test_service.average_of("John"), 3.75)

    @patch.object(NoteStorage, 'get_all_notes_of')
    def test_note_service_get_all_notes_of_no_notes_found(self, mock_method):
        mock_method.return_value = []
        test_service = NoteService()
        with self.assertRaisesRegex(ValueError, "No notes found"):
            test_service.average_of("John")

    def test_note_service_get_all_notes_of_name_not_a_string(self):
        test_service = NoteService()
        with self.assertRaisesRegex(TypeError, "Name must be a string"):
            test_service.average_of(['john'])

    @patch.object(NoteStorage, 'clear')
    def test_note_service_clear(self, mock_method):
        mock_method.return_value = True
        test_service = NoteService()
        self.assertEqual(test_service.clear(), True)


if __name__ == "__main__":
    unittest.main()

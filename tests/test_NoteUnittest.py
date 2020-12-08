from src.notes.Note import Note
import unittest

class TestNote(unittest.TestCase):
    def setUp(self):
        self.temp = Note("John", 4.2)

    def test_note_disallow_name_not_string(self):
        with self.assertRaisesRegex(TypeError, "Name must be a string"):
            Note({}, 2.43)

    def test_note_disallow_name_empty_string(self):
        with self.assertRaisesRegex(ValueError, "Name cannot be an empty string"):
            Note("", 2.31)

    def test_note_disallow_note_not_a_float(self):
        with self.assertRaisesRegex(TypeError, "Note must be a float type"):
            Note("xtz", 4)

    def test_note_disallow_note_lt_2(self):
        with self.assertRaisesRegex(ValueError, "Note must be in beteween 2 and 6"):
            Note("xtz", 1.99)

    def test_note_disallow_note_gt_6(self):
        with self.assertRaisesRegex(ValueError, "Note must be in beteween 2 and 6"):
            Note("xtz", 6.01)

    def test_note_get_name(self):
        name = self.temp.get_name()
        self.assertEqual(name, "John")

    def test_note_get_note(self):
        note = self.temp.get_note()
        self.assertEqual(note, 4.2)

    def tearDown(self):
        self.temp = None

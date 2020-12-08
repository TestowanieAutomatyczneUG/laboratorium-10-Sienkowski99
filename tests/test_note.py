import unittest
from src.sample.note import *

class TestNote(unittest.TestCase):

    def test_get_name_correct(self):
        self.assertEqual("Math", self.note.get_name())

    def test_get_name_wrong(self):
        self.assertNotEqual(2137, self.note.get_name())

    def test_get_note_correct(self):
        self.assertEqual(3.5, self.note.get_note())

    def test_get_note_wrong(self):
        self.assertNotEqual("siemanko witamw mojej kuchni", self.note.get_note())

    def test_init_empty_name(self):
        with self.assertRaises(ValueError):
            note = Note("", 4)

    def test_note_from_range(self):
        with self.assertRaises(ValueError):
            note = Note("eluwina", 2137)

    def test_note_name_not_str(self):
        with self.assertRaises(ValueError):
            note = Note([], 5)

    def setUp(self):
        self.note = Note("Math", 3.5)

    def tearDown(self):
        self.note = None

if __name__ == '__main__':
    unittest.main()

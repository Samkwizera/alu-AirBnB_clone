#!/usr/bin/python3
"""
This module contains test cases for the FileStorage class.
"""
import unittest
import os
import json
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up test cases."""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.user = User()
        self.state = State()
        self.city = City()
        self.amenity = Amenity()
        self.place = Place()
        self.review = Review()

    def tearDown(self):
        """Clean up after tests."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test the new method."""
        self.storage.new(self.base_model)
        key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test the save method."""
        self.storage.new(self.base_model)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as f:
            data = json.load(f)
            key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
            self.assertIn(key, data)

    def test_reload(self):
        """Test the reload method."""
        self.storage.new(self.base_model)
        self.storage.save()
        self.storage.reload()
        key = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        self.assertIn(key, self.storage.all())

    def test_reload_empty_file(self):
        """Test reload with empty file."""
        self.storage.save()
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_nonexistent_file(self):
        """Test reload with nonexistent file."""
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})


if __name__ == '__main__':
    unittest.main() 
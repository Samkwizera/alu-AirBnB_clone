#!/usr/bin/python3
"""
This module contains test cases for the Place class.
"""
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def setUp(self):
        """Set up test cases."""
        self.place = Place()

    def test_init(self):
        """Test initialization of Place."""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_inheritance(self):
        """Test that Place inherits from BaseModel."""
        self.assertIsInstance(self.place, Place)
        from models.base_model import BaseModel
        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == '__main__':
    unittest.main() 
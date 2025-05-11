#!/usr/bin/python3
"""
This module contains test cases for the Amenity class.
"""
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def setUp(self):
        """Set up test cases."""
        self.amenity = Amenity()

    def test_init(self):
        """Test initialization of Amenity."""
        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        """Test that Amenity inherits from BaseModel."""
        self.assertIsInstance(self.amenity, Amenity)
        from models.base_model import BaseModel
        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == '__main__':
    unittest.main() 
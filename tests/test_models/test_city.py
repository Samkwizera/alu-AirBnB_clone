#!/usr/bin/python3
"""
This module contains test cases for the City class.
"""
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        """Set up test cases."""
        self.city = City()

    def test_init(self):
        """Test initialization of City."""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_inheritance(self):
        """Test that City inherits from BaseModel."""
        self.assertIsInstance(self.city, City)
        from models.base_model import BaseModel
        self.assertTrue(issubclass(City, BaseModel))


if __name__ == '__main__':
    unittest.main() 
#!/usr/bin/python3
"""
This module contains test cases for the BaseModel class.
"""
import unittest
from datetime import datetime
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def setUp(self):
        """Set up test cases."""
        self.model = BaseModel()

    def test_init(self):
        """Test initialization of BaseModel."""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """Test string representation."""
        string = str(self.model)
        self.assertIn("[BaseModel]", string)
        self.assertIn(self.model.id, string)

    def test_save(self):
        """Test save method."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict(self):
        """Test to_dict method."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('id', model_dict)


if __name__ == '__main__':
    unittest.main() 
#!/usr/bin/python3
"""
This module contains test cases for the User class.
"""
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up test cases."""
        self.user = User()

    def test_init(self):
        """Test initialization of User."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_inheritance(self):
        """Test that User inherits from BaseModel."""
        self.assertIsInstance(self.user, User)
        from models.base_model import BaseModel
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == '__main__':
    unittest.main() 
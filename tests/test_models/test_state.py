#!/usr/bin/python3
"""
This module contains test cases for the State class.
"""
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def setUp(self):
        """Set up test cases."""
        self.state = State()

    def test_init(self):
        """Test initialization of State."""
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        """Test that State inherits from BaseModel."""
        self.assertIsInstance(self.state, State)
        from models.base_model import BaseModel
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == '__main__':
    unittest.main() 
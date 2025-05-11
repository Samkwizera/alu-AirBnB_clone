#!/usr/bin/python3
"""
This module contains test cases for the Review class.
"""
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def setUp(self):
        """Set up test cases."""
        self.review = Review()

    def test_init(self):
        """Test initialization of Review."""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        """Test that Review inherits from BaseModel."""
        self.assertIsInstance(self.review, Review)
        from models.base_model import BaseModel
        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == '__main__':
    unittest.main() 
#!/usr/bin/python3
"""
This module contains test cases for the console.py file.
"""
import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for the HBNBCommand class."""

    def setUp(self):
        """Set up test cases."""
        self.console = HBNBCommand()

    def test_quit_command(self):
        """Test the quit command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.do_quit(""))

    def test_EOF_command(self):
        """Test the EOF command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.do_EOF(""))

    def test_emptyline(self):
        """Test empty line input."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.emptyline()
            self.assertEqual(f.getvalue(), "")

    def test_help_command(self):
        """Test the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.do_help("")
            self.assertIn("Documented commands", f.getvalue())


if __name__ == '__main__':
    unittest.main() 
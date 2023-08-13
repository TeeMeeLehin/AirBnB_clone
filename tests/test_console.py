#!/usr/bin/python3
"""test script for the Console module"""
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand, clean_quotes


class TestConsole(unittest.TestCase):
    """The Test Class"""

    def setUp(self):
        "function to set up test class"
        self.console = HBNBCommand()

    def test_create(self):
        "testing the create function"
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertTrue(len(output) == 36)  # Checking if ID length is 36

    def test_show(self):
        "testing the show function"
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_show_invalid_class(self):
        "test function"
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show InvalidClass 123")
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_clean_quotes(self):
        "testing the clean_quotes function"
        self.assertEqual(clean_quotes('"text"'), "text")
        self.assertEqual(clean_quotes("text"), "text")


if __name__ == '__main__':
    unittest.main()

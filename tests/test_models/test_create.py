#!/usr/bin/python3
""" Unittest for console.py """
import unittest
from io import StringIO
from unittest.mock import patch
import os
from console import HBNBCommand
from models import storage
from models.engine.file_storage import FileStorage


blueprint = ["BaseModel", "User", "State", "City", "Amenity",
             "Place", "Review"]


class ConsoleTests(unittest.TestCase):
    """Unittests for Console"""
    def test_create_wrong(self):
        '''test for wrong create use'''
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual("** class name missing **", f.getvalue().strip())
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd("create a"))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

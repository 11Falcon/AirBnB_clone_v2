#!/usr/bin/python3
""" Module for testing console """
import unittest
import contextlib
import os
from console import HBNBCommand
from io import StringIO


class test_console(unittest.TestCase):
    """ Class to test the console file """
    def setUp(self):
        """Initialise the test"""
        self.output = StringIO()
        self.console = HBNBCommand(stdout=self.output)

    def test_help(self):
        """ Test help function """
        self.console.onecmd("help")
        output = self.output.getvalue()
        print("help output:\n", output)
        self.assertIn("Documented commands (type help <topic>):", output)

    def test_unknown_command(self):
        """Testing unknown command"""
        self.console.onecmd("testingFalcon")
        output = self.output.getvalue()
        self.assertIn("*** Unknown syntax: testingFalcon", output)

    def testUnknown_command(self):
        """ Testing unknown command """
        self.console.onecmd("testingFalcon")
        output = self.output.getvalue()
        self.assertIn("Unknown syntax: testingFalcon", output)

    def testEmptyLine(self):
        """ Testing an Empty Line"""
        self.console.onecmd("")
        output = self.output.getvalue()
        self.assertEqual(output, "")

    def test_EOF(self):
        """ Testing EOF command"""
        self.console.onecmd("EOF")
        output = self.output.getvalue()

    def test_Creat_count_City(self):
        """ Test creating, countingm and destroying a City"""

        f = StringIO()
        with contextlib.redirect_stdout(f):
            self.console.onecmd("count City")

        first_count = int(f.getvalue().strip())

        f = StringIO()
        with contextlib.redirect_stdout(f):
            self.console.onecmd('create City')

        city_id = f.getvalue().strip()

        f = StringIO()
        with contextlib.redirect_stdout(f):
            self.console.onecmd("count City")
        second_count = int(f.getvalue().strip())

        cm = f"show City {city_id}"
        f = StringIO()
        with contextlib.redirect_stdout(f):
            self.console.onecmd(cm)
        show_city_output = f.getvalue()

        cm = f"destroy City {city_id}"
        f = StringIO()
        with contextlib.redirect_stdout(f):
            self.console.onecmd(cm)

        f = StringIO()
        with contextlib.redirect_stdout(f):
            self.console.onecmd("count City")
        third_count = int(f.getvalue().strip())

        self.assertEqual(second_count - first_count, 1)
        self.assertEqual(second_count - third_count, 1)
        self.assertEqual(len(city_id), 36)
        self.assertIn(city_id, show_city_output)

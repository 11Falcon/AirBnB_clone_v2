#!/usr/bin/python3
""" Module for testing console """
import unittest
import os
import console
from io import StringIO


class test_console(unittest.TestCase):
    """ Class to test the console file """

    def setUP(self):
        """Initialisation """
        self.console = console.HBNBCommand

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, stdOut):
        """ Test help function """
        self.console.onecmd("help")
        output = stdOut.getvalue()
        self.assertIn("Documented commands (type help <topic>):", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_command(self, stdOut):
        """ Testing help <command> """
        self.console.onecmd("help update")
        output = stdOut.getvalue()
        self.assertIn("Updates an object with new information")

    @patch('sys.stdout', new_callable=StringIO)
    def testUnknown_command(self, stdOut):
        """ Testing unknown command """
        self.console.onecmd("testingFalcon")
        output = stdOut.getvalue()
        self.assertIn("*** Unknown syntax: testingFalcon")

    @patch('sys.stdout', new_callable=StringIO)
    def testEmptyLine(self, stdOut):
        """ Testing an Empty Line"""
        self.console.onecmd("")
        output = stdOut.getvalue()
        self.assertEqual(output, "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_EOF(self, stdOut):
        """ Testing EOF command"""
        self.console.onecmd("EOF")
        output = stdOut.getvalue()
        self.assertEqual(output, "\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_Create_count_City(self, stdOut):
        """testing creating a City
        counting number of cities
        testing destorying this city
        """
        self.console.onecmd("count City")
        first_count = stdOut.getvalue()
        self.console.onecmd("create City")
        city_id = stdOut.getvalue()
        self.console.onecmd("count City")
        second_count = stdOut.getvalue()
        self.console.onecmd("show City " + city_id)
        show_city_output = stdOut.getvalue()
        self.console.onecmd("destroy city" + city_id)
        sefl.console.onecmd("count City")
        third_count = stdOut.getvalue()
        self.assertEqual(int(second_count) - int(first_count), 1)
        self.assertEqual(int(second_count) - int(third_count), 1)
        self.assertEqual(len(city_id), 36)
        self.assertIn(city_id, show_city_output)

import unittest
from io import StringIO
import contextlib
from my_console import MyConsole

class TestMyConsole(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()
        self.console = MyConsole(stdout=self.output)

    def test_help(self):
        """Test help command output"""
        self.console.onecmd("help")
        output = self.output.getvalue()
        print("Captured help output:\n", output)
        self.assertIn("Documented commands (type help <topic>):", output)
        self.assertIn("hello", output)
        self.assertIn("exit", output)


if "__main__":
    unittest.main()

"""
Unit tests for py_file_resource package.
"""
import os
import unittest

from py_base_resource.py_file_resource import FileResource


class TestReadAndWrite(unittest.TestCase):
    """
    Tests for file reading and writing.
    """

    def setUp(self):
        self.fr = FileResource("test.txt")
        self.fr.create()
        self.fr.set_content("Line 1")

    def tearDown(self):
        self.fr.delete()

    def test1(self):
        """
        * Exit code equals 2
        * Can read file contents
        * Array length equals number of file lines
        """
        content = self.fr.read_content()
        self.assertEqual(2, self.fr.code)
        self.assertEqual(
            "Line 1", content[0].replace("\r", "").replace("\n", ""))
        self.assertEqual(1, len(content))

    def test2(self):
        """
        * Exit code equals 2
        * Can update file contents
        * Array length equals number of file lines
        """
        self.fr.set_content("Update Line 1")
        self.assertEqual(2, self.fr.code)

        content = self.fr.read_content()
        self.assertEqual(
            "Update Line 1", content[0].replace("\r", "").replace("\n", ""))
        self.assertEqual(1, len(content))

    def test3(self):
        """
        * Exit code equals 2
        * Can append file contents
        * Array length equals number of file lines
        """
        self.fr.append_content("Line 2")
        self.assertEqual(2, self.fr.code)

        content = self.fr.read_content()
        self.assertEqual(
            "Line 2", content[1].replace("\r", "").replace("\n", ""))
        self.assertEqual(2, len(content))


class TestCreateAndDelete(unittest.TestCase):
    """
    Tests for file creation and deletion
    """

    def setUp(self):
        self.fr = FileResource("test.txt")
        self.fr.create()

    def tearDown(self):
        self.fr.delete()

    def test1(self):
        """
        * Can create file if it does not exists
        * Exit code equals 2
        * Number of file lines equals 0

        * Can delete file if it exists
        * Exit code equals 2
        """
        fr = FileResource("new_file.txt")
        fr.create()
        self.assertEqual(2, fr.code)
        self.assertTrue(os.path.isfile("new_file.txt"))

        content = fr.read_content()
        self.assertEqual(0, fr.code)
        self.assertEqual(0, len(content))

        fr.delete()
        self.assertEqual(2, fr.code)
        self.assertFalse(os.path.isfile("new_file.txt"))

    def test2(self):
        """
        * If file already exists exit code equals 0 when invoke create method.
        * If file does not exists exit code equals 0 when invoke delete method.
        """
        self.fr.create()
        self.assertEqual(0, self.fr.code)

        self.fr.delete()
        self.fr.delete()
        self.assertEqual(0, self.fr.code)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

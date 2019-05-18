# -*- coding: utf-8 -*-
import os
import unittest

from py_directory_resource import DirectoryResource


class TestDirectoryResource(unittest.TestCase):
    def test1(self):
        """
        * Can create directory which contains parent directories if it does not exist
        * Exit code equals 2

        * Can delete directories which contain sub empty directories
        * Exit code equals 2
        """
        dr = DirectoryResource("parent/sub1/sub2")
        dr.create()
        self.assertEqual(2, dr.code)
        self.assertTrue(os.path.isdir("parent/sub1/sub2"))

        dr.delete()
        self.assertEqual(2, dr.code)
        self.assertFalse(os.path.isdir("parent"))

    def test2(self):
        """
        * If directory already exists exit code equals 0 when invoke create method.
        * If directory does not exist exit code equals 0 when invoke delete method.
        """
        dr = DirectoryResource("test_dir")
        dr.create()
        dr.create()
        self.assertEqual(0, dr.code)

        dr.delete()
        dr.delete()
        self.assertEqual(0, dr.code)

    def test3(self):
        """
        * Exit code equals 2
        * Array length equals number of files and directories
        """
        dr = DirectoryResource("resources")
        files = dr.get_files()
        self.assertEqual(2, dr.code)
        self.assertEqual(2, len(files))
        self.assertIn("test_dir", files)
        self.assertIn("test.txt", files)

    def test4(self):
        """
        * If target directory is empty exit code equals 0
        """
        dr = DirectoryResource("resources/test_dir")
        files = dr.get_files()
        self.assertEqual(0, dr.code)
        self.assertEqual(0, len(files))


if __name__ == "__main__":
    unittest.main()

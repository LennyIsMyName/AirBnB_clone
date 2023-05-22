#!/usr/bin/python3

from models.engine.file_storage import FileStorage
import unittest


class StorageTester(unittest.TestCase):
    def setUp(self):
        self.tester = FileStorage()

    def test_all(self):
        var = self.tester.all()
        self.assertTrue(var)

    def test_new(self):
        pass
    def test_save(self):
        pass

    def test_reload(self):
        pass

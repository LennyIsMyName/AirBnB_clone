#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.prototype = BaseModel()
        print('set up')
        
    def test_save(self):
        obj1 = self.prototype.updated_at
        self.prototype.save()
        obj2 = self.prototype.updated_at
        self.assertNotEqual(obj1, obj2)
    def test_to_dict(self):
        self.assertIsInstance(self.prototype.to_dict(), dict)

    def test___str__(self):
        self.assertIsInstance(self.prototype.__str__(), str)

    def test___init__(self):
        prototype = BaseModel(my_buddy='Tonny')
        self.assertEqual('Tonny', prototype.my_buddy)
        self.assertTrue(BaseModel.id)
        

if __name__ == '__main__':
    unittest.main()

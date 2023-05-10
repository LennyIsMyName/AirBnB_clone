#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    test_model = BaseModel()
    
    def check_to_dict_return_type(self):
        self.assertIsInstance(test_model.to_dict(), dict)

    def check_str_return_type(self):
        self.assertIsInstance(test_model.__str__(), str)

    def check_save(self):
        test_model.update_at()
        def compare_datetime(self):
            self.assertNotEqual(test_model.create_at, test_model.update_at)

    def check_len_of_datetime(self):
        self.assertEqual(len(test_model.created_at, 26))
        self.assertEqual(len(test_model.updated_at, 26))

    


if __name__ == '__main__':
    unittest.main()

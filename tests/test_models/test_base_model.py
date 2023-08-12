#!/usr/bin/python3
"""test script for the BaseModel class"""
import unittest
import datetime
import uuid
from models.base_model import BaseModel


class TestBaseModelInit(unittest.TestCase):
    """Testing the initialization of the BaseModel class"""

    def test_initialized_values_no_kwargs(self):
        "function testing initialized values called with no kwargs"
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)

    def test_initialization_with_kwargs(self):
        "function testing initialized values called with kwargs"
        created_at = datetime.datetime(2023, 8, 8, 12, 0, 0).isoformat()
        updated_at = datetime.datetime(2023, 8, 8, 12, 30, 0).isoformat()
        kwargs = {
            'id': 'some_id_value',
            'created_at': created_at,
            'updated_at': updated_at
        }
        obj = BaseModel(**kwargs)

        self.assertEqual(obj.id, 'some_id_value')
        self.assertEqual(obj.created_at, datetime.datetime.fromisoformat(created_at))
        self.assertEqual(obj.updated_at, datetime.datetime.fromisoformat(updated_at))

    def test_id_generation(self):
        "function testing the datetime attribute"
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_and_updated_at(self):
        "function testing the created and updated_at attributes"
        obj = BaseModel()
        self.assertLessEqual(obj.created_at, obj.updated_at)


class TestBaseModelMethods(unittest.TestCase):
    """Testing BaseModel methods"""

    def setUp(self):
        "instantiating a model instance"
        self.obj = BaseModel()

    def test_str_representation(self):
        "function to test the __str__ method"
        objj = self.obj
        expected_str = f"[{type(objj).__name__}] ({objj.id}) {objj.__dict__}"
        self.assertEqual(str(objj), expected_str)

    def test_save_method_updates_updated_at(self):
        "function to test the save method functionality"
        initial_updated_at = self.obj.updated_at
        self.obj.save()
        self.assertNotEqual(initial_updated_at, self.obj.updated_at)

    def test_to_dict_method(self):
        "function to test the serialization method"
        o_dict = self.obj.to_dict()
        self.assertIsInstance(o_dict, dict)
        self.assertEqual(o_dict['__class__'], type(self.obj).__name__)


if __name__ == '__main__':
    unittest.main()

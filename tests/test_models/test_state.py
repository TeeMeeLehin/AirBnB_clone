#!/usr/bin/python3
"""test script for the State class"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage


class TestState(unittest.TestCase):
    "Test class for the State class"
    def setUp(self):
        "Reset the objects dictionary before each test"
        storage.__objects = {}

    def test_inheritance(self):
        "testing the inheritance functionality"
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertIsInstance(state, State)

    def test_attributes(self):
        "testing the attributes"
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_attribute_default(self):
        "testing the default attributes"
        state = State()
        self.assertEqual(state.name, "")

    def test_attribute_assignment(self):
        "tetsing the assignment of class attributes"
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_save_method(self):
        "testing the inherited save method"
        state = State()
        prev_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(prev_updated_at, state.updated_at)

    def test_to_dict_method(self):
        "testing the inherited to_dict method"
        state = State()
        state.name = "Ondo"
        state.save()
        state_dict = state.to_dict()

        self.assertIsInstance(state_dict, dict)
        self.assertIn('__class__', state_dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertIn('id', state_dict)
        self.assertIn('created_at', state_dict)
        self.assertIn('updated_at', state_dict)
        self.assertIn('name', state_dict)


if __name__ == '__main__':
    unittest.main()

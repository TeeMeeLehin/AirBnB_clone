#!/usr/bin/python3
"""test script for the User class"""
import unittest
from models.base_model import BaseModel
from models.user import User
from models import storage


class TestUser(unittest.TestCase):
    """Test Class for the User class"""

    def setUp(self):
        "Reset the objects dictionary before each test"
        storage.__objects = {}

    def test_inheritance(self):
        "testing the inheritance functionality"
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertIsInstance(user, User)

    def test_attributes(self):
        "testing the user class attributes"
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_attribute_defaults(self):
        "testing that the default user class attributes"
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_attribute_assignment(self):
        "testing the class atrribute assignments"
        user = User()
        user.email = "test@example.com"
        user.password = "secure_password"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "secure_password")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_save_method(self):
        "testing the inherited save method"
        user = User()
        prev_updated_at = user.updated_at
        user.save()
        self.assertNotEqual(prev_updated_at, user.updated_at)

    def test_to_dict_method(self):
        "testing the inherited to_dict method"
        user = User()
        user.first_name = "Timi"
        user.last_name = "Turner"
        user.email = "timiturner@airbnb.co"
        user.password = "12345"
        user_dict = user.to_dict()

        self.assertIsInstance(user_dict, dict)
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('email', user_dict)
        self.assertIn('password', user_dict)
        self.assertIn('first_name', user_dict)
        self.assertIn('last_name', user_dict)


if __name__ == '__main__':
    unittest.main()

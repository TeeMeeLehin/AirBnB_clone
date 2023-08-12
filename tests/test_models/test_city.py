#!/usr/bin/python3
"""test script for the City class"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models import storage


class TestCity(unittest.TestCase):
    """Test class for the City class"""

    def setUp(self):
        " Reset the objects dictionary before each test"
        storage.__objects = {}

    def test_inheritance(self):
        "testing the inheritance functionality"
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertIsInstance(city, City)

    def test_attributes(self):
        "testing the attributes"
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_attribute_defaults(self):
        "testing the default attributes"
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attribute_assignment(self):
        "testing the assignment of attributes"
        city = City()
        city.state_id = "state_123"
        city.name = "City Name"
        self.assertEqual(city.state_id, "state_123")
        self.assertEqual(city.name, "City Name")

    def test_save_method(self):
        "testing the inherited save method"
        city = City()
        prev_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(prev_updated_at, city.updated_at)

    def test_to_dict_method(self):
        "testing the inherited to_dict method"
        city = City()
        city.name = "Akure"
        city.state_id = "Ondo"
        city.save()
        city_dict = city.to_dict()

        self.assertIsInstance(city_dict, dict)
        self.assertIn('__class__', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('state_id', city_dict)
        self.assertIn('name', city_dict)


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""test script for the Place class"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from models import storage


class TestPlace(unittest.TestCase):
    """Test class for the place class"""

    def setUp(self):
        """Reset the objects dictionary before each test"""
        storage.__objects = {}

    def test_inheritance(self):
        """Test if Place class inherits from BaseModel"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertIsInstance(place, Place)

    def test_attributes(self):
        """Test if Place class has expected attributes"""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))

    def test_attribute_defaults(self):
        """Test if Place class attributes have correct default values"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")

    def test_attribute_assignment(self):
        """Test attribute assignment for Place class"""
        place = Place()
        place.city_id = "city_123"
        place.user_id = "user_123"
        place.name = "My Place"

        self.assertEqual(place.city_id, "city_123")
        self.assertEqual(place.user_id, "user_123")
        self.assertEqual(place.name, "My Place")

    def test_save_method(self):
        """Test save method in Place class"""
        place = Place()
        prev_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(prev_updated_at, place.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method in Place class"""
        place = Place()
        place_dict = place.to_dict()

        self.assertIsInstance(place_dict, dict)
        self.assertIn('__class__', place_dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)


if __name__ == '__main__':
    unittest.main()

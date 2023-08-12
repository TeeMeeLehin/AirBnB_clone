#!/usr/bin/python3
"""test script for the Amenity class"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage


class TestAmenity(unittest.TestCase):
    """Test class for the amenity class"""

    def setUp(self):
        # Reset the objects dictionary before each test
        storage.__objects = {}

    def test_inheritance(self):
        """Test if Amenity class inherits from BaseModel"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertIsInstance(amenity, Amenity)

    def test_attributes(self):
        """Test if Amenity class has expected attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))

    def test_attribute_default(self):
        """Test if Amenity class attribute has correct default value"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_attribute_assignment(self):
        """Test attribute assignment for Amenity class"""
        amenity = Amenity()
        amenity.name = "Swimming Pool"
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_save_method(self):
        """Test save method in Amenity class"""
        amenity = Amenity()
        prev_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(prev_updated_at, amenity.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method in Amenity class"""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()

        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('__class__', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)


if __name__ == '__main__':
    unittest.main()

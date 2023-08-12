#!/usr/bin/python3
"""test script for the Review class"""
import unittest
from models.base_model import BaseModel
from models.review import Review
from models import storage


class TestReview(unittest.TestCase):
    """Test class for the review class"""

    def setUp(self):
        """Reset the objects dictionary before each test"""
        storage.__objects = {}

    def test_inheritance(self):
        """Test if Review class inherits from BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertIsInstance(review, Review)

    def test_attributes(self):
        """Test if Review class has expected attributes"""
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_attribute_defaults(self):
        """Test if Review class attributes have correct default values"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_attribute_assignment(self):
        """Test attribute assignment for Review class"""
        review = Review()
        review.place_id = "place_123"
        review.user_id = "user_123"
        review.text = "Nice place to stay"
        self.assertEqual(review.place_id, "place_123")
        self.assertEqual(review.user_id, "user_123")
        self.assertEqual(review.text, "Nice place to stay")

    def test_save_method(self):
        """Test save method in Review class"""
        review = Review()
        prev_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(prev_updated_at, review.updated_at)

    def test_to_dict_method(self):
        """Test to_dict method in Review class"""
        review = Review()
        review_dict = review.to_dict()

        self.assertIsInstance(review_dict, dict)
        self.assertIn('__class__', review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)


if __name__ == '__main__':
    unittest.main()

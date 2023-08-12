#!/usr/bin/python3
"""test script for the FileStorage class"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Class Test Module for the FileStorage Class"""

    def test_all(self):
        "testing the all method"
        self.assertEqual(type(storage.all()), dict)

    def test_new(self):
        "testing the new method"
        model = BaseModel()
        model.name = "Tester"
        model.save()
        search = f"BaseModel.{model.id}"
        storage.new(model)
        self.assertEqual((storage.all()[search].name), "Tester")

    def test_save(self):
        "testing the save method"
        num = len(storage.all())
        model = BaseModel()
        model.save()

        self.assertEqual(len(storage.all()), num + 1)

    def test_reload(self):
        "testing the reload method"
        model = BaseModel()
        model.name = "Test Model"
        model.save()

        new_storage = FileStorage()
        new_storage.reload()

        loaded_model = new_storage.all()["BaseModel." + model.id]
        self.assertEqual(loaded_model.name, "Test Model")


if __name__ == '__main__':
    unittest.main()

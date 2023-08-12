#!/usr/bin/python3
"Module to define the Basemodel class"
import uuid
import datetime
from . import storage


class BaseModel():
    """The BaseModel Class with its attendant methods"""

    def __init__(self, *args, **kwargs):
        "the initialization function"
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        else:
            self.__dict__.update(kwargs)
            ct = self.__dict__['created_at']
            new_ct = datetime.datetime.fromisoformat(ct)
            self.__dict__['created_at'] = new_ct

            ut = self.__dict__['updated_at']
            new_ut = datetime.datetime.fromisoformat(ut)
            self.__dict__['updated_at'] = new_ut

    def __str__(self):
        "function modifying the class' self-representation string"
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        "function to save or update a class instance"
        self.updated_at = datetime.datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        "function to serialize the class to a json-like object"
        dictt = self.__dict__.copy()
        dictt['__class__'] = type(self).__name__
        dictt['created_at'] = dictt['created_at'].isoformat()
        dictt['updated_at'] = dictt['updated_at'].isoformat()
        return dictt

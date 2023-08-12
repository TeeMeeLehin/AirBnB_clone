#!/usr/bin/python3
"Module to define the FileStorage class"
import json
import os


class FileStorage():
    """The FileStorage class with its attendant methods and attributes"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        "function that returns the dictionary - __objects"
        return self.__objects

    def new(self, obj):
        "function saves new obj into __onjects dictionary"
        class_name = type(obj).__name__
        obj_key = f"{class_name}.{obj.id}"
        dictt = {obj_key: obj}
        self.__objects.update(dictt)

    def save(self):
        "function to serialize __objects to JSON file"
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.__file_path, "w") as file:
            file.write(json.dumps(serialized_objects))

    def reload(self):
        "function to deserialize JSON file to __objects dictionary"
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.review import Review
        from models.place import Place
        from models.amenity import Amenity

        if os.path.isfile(self.__file_path):
            try:
                with open(self.__file_path, 'r') as json_file:
                    data = json.load(json_file)
                    for key, value in data.items():
                        class_name = eval(key.split(".")[0])
                        value.pop('__class__')
                        new_obj = class_name(**value)
                        self.__objects[key] = new_obj
            except json.JSONDecodeError:
                self.__objects = {}

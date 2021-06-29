#!/usr/bin/python3

'Contains the FileStorage class'

import json
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity


class FileStorage:
    'that serializes instances to a JSON file and deserialize'

    __file_path = "file.json"
    __objects = {}

    def all(self):
        'returns the dictionary'
        return FileStorage.__objects
    def new(self, obj):
        'sets in __objects the obj with key <obj class name>.id'
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj
    def save(self):
        'serializes __objects to the JSON file (path: __file_path)'
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)
    def reload(self):
        'deserializes the JSON file to __objects'
        try:
            with open(self.__file_path, 'r') as f:
                obj_js = json.load(f)
            for key, value in obje_js.items():
                self.__objects[key] = eval(key.split('.')[0])(**value)
        except:
            pass
        
        

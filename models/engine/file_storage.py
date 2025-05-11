#!/usr/bin/python3
"""
This module contains the FileStorage class that handles serialization
and deserialization of objects to/from JSON.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Class for serializing and deserializing objects to/from JSON."""
    
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects
    
    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj
    
    def save(self):
        """Serialize __objects to the JSON file."""
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()
        
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(obj_dict, f)
    
    def reload(self):
        """Deserialize the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    del value['__class__']
                    if class_name == 'BaseModel':
                        self.__objects[key] = BaseModel(**value)
                    elif class_name == 'User':
                        self.__objects[key] = User(**value)
                    elif class_name == 'State':
                        self.__objects[key] = State(**value)
                    elif class_name == 'City':
                        self.__objects[key] = City(**value)
                    elif class_name == 'Amenity':
                        self.__objects[key] = Amenity(**value)
                    elif class_name == 'Place':
                        self.__objects[key] = Place(**value)
                    elif class_name == 'Review':
                        self.__objects[key] = Review(**value)
        except FileNotFoundError:
            pass 
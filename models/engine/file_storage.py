#!/usr/bin/python3
"""This establishes the FileStorage class."""
import json
from models.base_model import BaseModel
from os import path
from models.user import User


class FileStorage:
    """This signifies an abstract storage engine.

    Attr:
        __file_path (str): The filename used for storing objects.
        __objects (dict): A collection of instantiated objects in the
        form of a dictionary..
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Provide the "__objects" dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """Add the "obj" with the key "<obj_class_name>.id"
        into the "__objects" dictionary.
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize the "__objects" to the JSON file specified
        in "__file_path.
        """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file located at "__file_path"
        into "__objects" if it is present.
        """
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

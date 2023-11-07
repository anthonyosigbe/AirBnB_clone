#!/usr/bin/python3
"""This establishes the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """This signifies the foundational BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Base Model init Method

        Within this section, the initial values for a,
        Base Model instance are set as defaults.
        """
        if kwargs:
            for arg, val in kwargs.items():
                if arg in ('created_at', 'updated_at'):
                    val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')

                if arg != '__class__':
                    setattr(self, arg, val)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()

    def __str__(self):
        """Provide the printed or string representation,
        of the BaseModel instance.
        """
        classlabel = self.__class__.__name__
        return "[{0}] ({1}) {2}".format(classlabel, self.id, self.__dict__)

    def save(self):
        """Update the "updated_at" field with the current date and time."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Provide the dictionary representation of the BaseModel instance,

        which contains the key/value pair "class"
        representing the object's class name.
        """
        record = self.__dict__.copy()
        record["created_at"] = self.created_at.isoformat()
        record["updated_at"] = self.updated_at.isoformat()
        record["__class__"] = self.__class__.__name__

        return record

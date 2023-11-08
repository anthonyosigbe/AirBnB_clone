#!/usr/bin/python3
"""Depicts the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Att:
        name (str): The name of the amenity.
    """

    name = ""

#!/usr/bin/python3
"""
This module contains the Amenity class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class for storing amenity information."""
    
    name = "" 
#!/usr/bin/python3
"""
This module contains the Review class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class for storing review information."""
    
    place_id = ""
    user_id = ""
    text = "" 
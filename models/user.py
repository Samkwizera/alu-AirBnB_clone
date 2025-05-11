#!/usr/bin/python3
"""
This module contains the User class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class for storing user information."""
    
    email = ""
    password = ""
    first_name = ""
    last_name = "" 
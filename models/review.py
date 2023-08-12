#!/usr/bin/python3
"Module to define the Review class"
from models.base_model import BaseModel


class Review(BaseModel):
    """The Review class with its public attributes"""

    place_id = ""
    user_id = ""
    text = ""

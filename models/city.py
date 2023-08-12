#!/usr/bin/python3
"Module to define the City class"
from models.base_model import BaseModel


class City(BaseModel):
    """The City class with its public attributes"""

    state_id = ""
    name = ""

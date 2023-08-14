#!/usr/bin/python3
"""Module to define class state that inherits from class BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class State
        Public Instance:
            name: empty string
    """
    name = ""

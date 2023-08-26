#!/usr/bin/python3
"""User class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Clas for managing city objects"""

    state_id = ""
    name = ""

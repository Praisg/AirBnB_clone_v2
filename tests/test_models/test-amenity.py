#!/usr/bin/python3
"""Unittest  for the Amenity Class."""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import os
import json
from models.engine.file_storage import FileStorage
import re
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    """TestCases for the Amenity class."""

    def setUp(self):
        """Setup test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets File-Storage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of Amenity class."""

        b = Amenity()
        self.assertEqual(str(type(b)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(b, Amenity)
        self.assertTrue(issubclass(type(b), BaseModel))

    def test_8_attributes(self):
        """Tests attributes of Amenity class."""
        attributes = storage.attributes()["Amenity"]
        o = Amenity()
        for k, v in attributes.items():
            self.assertTrue(hasattr(o, k))
            self.assertEqual(type(getattr(o, k, None)), v)


if __name__ == "__main__":
    unittest.main()

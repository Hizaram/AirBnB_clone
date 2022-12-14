#!/usr/bin/python3
'''
    Testing the file_storage module.
'''

import os
import time
import json
import unittest
from models.base_model import BaseModel
from models.state import State
from models.engine.file_storage import FileStorage


class testFileStorage(unittest.TestCase):
    '''
        Testing the FileStorage class
    '''

    def setUp(self):
        '''
            Initializing classes
        '''
        self.storage = FileStorage()
        self.my_model = BaseModel()

    def tearDown(self):
        '''
            Cleaning up.
        '''

        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_return_type(self):
        '''
            Tests the data type of the return value of the all method.
        '''
        storage_all = self.storage.all()
        self.assertIsInstance(storage_all, dict)

    def test_save_file_exists(self):
        '''
            Tests that a file gets created with the name file.json
        '''
        self.storage.save()
        self.assertTrue(os.path.isfile("file.json"))

    def test_save_file_read(self):
        '''
            Testing the contents of the files inside the file.json
        '''
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = json.load(fd)

        self.assertTrue(isinstance(content, dict))

    def test_the_type_file_content(self):
        '''
            testing the type of the contents inside the file.
        '''
        self.storage.save()
        self.storage.new(self.my_model)

        with open("file.json", encoding="UTF8") as fd:
            content = fd.read()

        self.assertIsInstance(content, str)

    def test_reaload_without_file(self):
        '''
            Tests that nothing happens when file.json does not exists
            and reload is called
        '''

        try:
            self.storage.reload()
            self.assertTrue(True)
        except BaseException:
            self.assertTrue(False)

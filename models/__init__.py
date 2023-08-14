#!/usr/bin/python3
"""This module instantiates an object of class fileStorage"""
from models.engine.file_store import FileStorage

storage = FileStorage()
storage.reload()

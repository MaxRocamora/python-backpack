# ----------------------------------------------------------------------------------------
# Python-Backpack - JsonMetadata
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------
import sys
import os
import time
import inspect
from datetime import datetime
import platform

from backpack.json_utils import json_load, json_save
from backpack.version import version


class JsonMetaFile():

    def __init__(self, name: str, path: str):
        '''saves/load a class/dict as a json metadata file

        Args:
            name (str): name of the file/class
            path (str, optional): filepath. Defaults to None.
        '''
        self._name = name
        self._path = path
        self._data = {}
        self._data["_about"] = {'package': 'python-backpack',
                                'version': self.version}

    # ------------------------------------------------------------------------------------
    # PROPERTIES
    # ------------------------------------------------------------------------------------

    @property
    def name(self):
        ''' name of this metadata class'''
        return self._name

    @property
    def version(self):
        ''' version of this metadata class'''
        return version

    @property
    def data(self):
        ''' stored metadata dict '''
        return self._data

    @data.setter
    def data(self, val):
        self._data = val

    @property
    def prefix(self):
        ''' file prefix, is auto-included on the filename '''
        return "MD_"

    @property
    def filename(self):
        ''' Returns default filename with prefix and extension '''
        return self.prefix + self.name + '.json'

    @property
    def filepath(self):
        ''' full json metadata filepath '''
        return os.path.join(self.path, self.filename)

    @property
    def path(self):
        ''' base path location of metadata json file '''
        return self._path

    def has_file(self):
        return os.path.exists(self.filepath)

    # ------------------------------------------------------------------------------------
    # LOAD/INSERT/REMOVE/SAVE
    # ------------------------------------------------------------------------------------

    def load(self):
        ''' loads metadata from disk '''
        self._data = json_load(self.filepath) if self.has_file() else {}

    def insert(self, key, value):
        ''' inserts value into metadata '''
        self._data[key] = value

    def remove(self, key):
        ''' remove key from metadata '''
        if key in self._data.keys():
            del self._data[key]

    def save(self, path: str = None):
        ''' Save current metadata into json file.
        Args:
            path (str) sets target path for json file. Optional. Defaults to None
        '''
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        self.data['system'] = self._system_data()
        json_save(self.data, self.filepath)

    # ------------------------------------------------------------------------------------
    # CLASS MODE METHODS
    # ------------------------------------------------------------------------------------

    def load_as_class(self):
        ''' returns the metadata dict as a class obj '''
        metadataClass = type(self.name, (), self._data)
        return metadataClass

    def insert_class(self, _class):
        ''' set class dict to data, data is cleared '''
        self.data = self._attributes_from_class(_class)

    def _attributes_from_class(self, _class):
        attributes = {}
        for name in dir(_class):
            value = getattr(_class, name)
            if not name.startswith('__') and not inspect.ismethod(value):
                attributes[name] = value
        return attributes

    # ------------------------------------------------------------------------------------
    # SYSTEM METADATA OS/USER/TIME
    # ------------------------------------------------------------------------------------

    def _system_data(self):
        ''' add system metadata to the default data before save '''
        return {
            'name': self.name,
            'app': os.path.basename(sys.executable),
            'PC': str(platform.node()),
            'python_version': sys.version,
            'User': str(os.getenv('username')),
            'time': self._get_time_metadata,
        }

    @property
    def _get_time_metadata(self):
        ''' Get export time info. '''
        ftime = time.strftime("%Y,%b,%d,%j,%H:%M", time.localtime())
        times = ftime.split(",")
        td = {
            "year": times[0],
            "month": times[1],
            "day": times[2],
            "year_day": times[3],
            "time": times[4],
            'save_time': datetime.now().ctime()
        }
        return td

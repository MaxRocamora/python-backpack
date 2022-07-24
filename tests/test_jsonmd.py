# ----------------------------------------------------------------------------------------
# Python-Backpack - JsonMD Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import contextlib
from backpack.json_metadata import JsonMetaFile

import unittest
import os
import sys

mod_path = os.path.dirname(__file__)
if mod_path not in sys.path:
    sys.path.append(mod_path)


# test path & name
TEST_PATH = os.path.join(mod_path, 'test_json')
NAME = 'test'
CLASS_NAME = 'proxy'
ATTRIBUTES = ['foo', 'bar']


class Test_windows(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        # remove test files
        with contextlib.suppress(OSError):
            # os.remove(temp_update_json_test_file)
            # os.remove(test_json_file)
            pass

    def test_metadata(self):
        ''' testing module '''
        meta = JsonMetaFile(NAME, TEST_PATH)

        # test properties
        self.assertEqual(meta.name, NAME)

        meta.insert(key='coins', value=12)

        # check if data have coins and value 12
        self.assertEqual(meta.data['coins'], 12)

        meta.save()

        # file was created
        self.assertEqual(meta.has_file(), True)

        # check if file exists
        self.assertEqual(os.path.exists(meta.filepath), True)

        meta.insert('coins', 7)

        # check if data have coins and value 7
        self.assertEqual(meta.data['coins'], 7)

        meta.remove('coins')
        self.assertEqual(meta.data.get('coins', None), None)

        meta.insert(key='items', value=ATTRIBUTES)
        meta.save()

        # load
        metaObj = meta.load_as_class()
        self.assertEqual(type(metaObj), type)
        self.assertEqual(hasattr(metaObj, 'items'), True)
        self.assertEqual(metaObj.items, ATTRIBUTES)

        # load class
        meta = JsonMetaFile(NAME, TEST_PATH)
        meta.load()

    def test_create_from_class(self):
        ''' save_from_a_class '''
        meta = JsonMetaFile(NAME, TEST_PATH)
        self.assertEqual(meta.name, NAME)

        proxyClass = type('Proxy', (), {'foo': 12, 'items': ATTRIBUTES})
        meta.insert_class(proxyClass)
        self.assertEqual(meta.data['foo'], 12)
        self.assertEqual(meta.data['items'], ATTRIBUTES)
        meta.save()


if __name__ == '__main__':
    unittest.main()

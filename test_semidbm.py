#!/usr/bin/env python

import os
import unittest
import tempfile
import StringIO

import semidbm


class TestSemiDBM(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.mkdtemp(prefix='semidbm_ut')

    def tearDown(self):
        for f in os.listdir(self.tempdir):
            os.remove(os.path.join(self.tempdir, f))
        os.rmdir(self.tempdir)

    def open_db_file(self):
        return semidbm.open(os.path.join(self.tempdir,
                                         'myfile.db'), 'c')

    def test_insert_then_retrieve(self):
        db = self.open_db_file()
        db['foo'] = 'bar'
        self.assertEqual(db['foo'], 'bar')

    def test_insert_close_retrieve(self):
        # This will verify loading the index.
        db = self.open_db_file()
        db['foo'] = 'bar'
        db.close()

        db2 = self.open_db_file()
        self.assertEqual(db2['foo'], 'bar')

    def test_insert_multiple(self):
        db = self.open_db_file()
        db['one'] = '1'
        db['two'] = '2'
        db['three'] = '3'
        self.assertEqual(db['one'], '1')
        self.assertEqual(db['two'], '2')
        self.assertEqual(db['three'], '3')

    def test_intermixed_inserts_and_retrievals(self):
        db = self.open_db_file()
        db['one'] = '1'
        db['two'] = '2'
        self.assertEqual(db['one'], '1')
        db['three'] = '3'
        self.assertEqual(db['two'], '2')
        self.assertEqual(db['three'], '3')

    def test_keyerror_raised_when_key_does_not_exist(self):
        db = self.open_db_file()
        self.assertRaises(KeyError, db.__getitem__, 'one')

    def test_updates(self):
        db = self.open_db_file()
        db['one'] = 'foo'
        db['one'] = 'bar'
        self.assertEqual(db['one'], 'bar')
        db['one'] = 'baz'
        self.assertEqual(db['one'], 'baz')

    def test_updates_persist(self):
        db = self.open_db_file()
        db['one'] = 'foo'
        db['one'] = 'bar'
        db['one'] = 'baz'
        db.close()

        db2 = self.open_db_file()
        self.assertEqual(db2['one'], 'baz')

    def test_contains(self):
        db = self.open_db_file()
        db['one'] = 'foo'
        self.assertTrue('one' in db)

    def test_deletes(self):
        db = self.open_db_file()
        db['foo'] = 'bar'
        del db['foo']
        self.assertTrue('foo' not in db)

    def test_delete_key_not_there_when_reopened(self):
        db = self.open_db_file()
        db['foo'] = 'foo'
        db['bar'] = 'bar'
        del db['foo']
        db.close()

        db2 = self.open_db_file()
        self.assertTrue('foo' not in db2)
        self.assertEqual(db2['bar'], 'bar')


if __name__ == '__main__':
    unittest.main()
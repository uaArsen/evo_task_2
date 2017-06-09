# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.test.runner import DiscoverRunner

import unittest
from django.test import Client
from utils import *


class DatabaselessTestRunner(DiscoverRunner):
    """A test suite runner that does not set up and tear down a database."""

    def setup_databases(self):
        """Overrides DjangoTestSuiteRunner"""
        pass

    def teardown_databases(self, *args):
        """Overrides DjangoTestSuiteRunner"""
        pass


def print_test_name(test):
    print "In method", test._testMethodName


class AppTest(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        """clean every keys that we have been created"""
        flush_all()

    def setUp(self):
        """doing base setup"""
        print_test_name(self)
        self.variable = "somekey"
        self.client = Client()

    def test01_set_variable(self):
        """test set key"""
        self.assertEquals(True, set_variable(self.variable, 1, TEST_POOL))

    def test02_get_variable(self):
        """test get key"""
        self.assertEquals("1", get_variable(self.variable, TEST_POOL))

    def test03_increment_existing_variable(self):
        """test increment existing key"""
        self.assertEquals(2, increment_or_initialize(self.variable, TEST_POOL))
        self.assertEquals("2", get_variable(self.variable, TEST_POOL))

    def test04_delete_variable(self):
        """test increment existing key"""
        self.assertEquals(True, delete_variable(self.variable, TEST_POOL))

    def test05_increment_not_existing_variable(self):
        """test increment non existing key"""
        not_exist = self.variable + "not_exist"
        self.assertEquals(1, increment_or_initialize(not_exist, TEST_POOL))
        self.assertEquals("1", get_variable(not_exist, TEST_POOL))

    def test06_index(self):
        """test view / just check status code"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test07_index(self):
        """test view / just check status code"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
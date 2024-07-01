#!/usr/bin/env python3
""" Unit tests for utils module
"""
import unittest
from parameterized import parameterized
from typing import Mapping, Sequence
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Test class for utils.access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected: any):
        """ Test output of utils.access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

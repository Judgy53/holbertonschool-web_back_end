#!/usr/bin/env python3
""" Unit tests for utils module
"""
import unittest
from unittest.mock import patch, MagicMock, Mock
from parameterized import parameterized
from typing import Mapping, Sequence, Dict
from utils import access_nested_map, get_json


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

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence,
                                         msg: str):
        """ Test exceptions of utils.access_nested_map
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), msg)


class TestGetJson(unittest.TestCase):
    """ Test class for utils.get_json
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict):
        """ Test output of utils.get_json
        """
        with patch("utils.requests.get") as mock_get:
            mock_return = Mock()
            mock_return.json.return_value = test_payload
            mock_get.return_value = mock_return

            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)

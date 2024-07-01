#!/usr/bin/env python3
""" Unit tests for client module
"""
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Tests for the GithubOrgClient class
    """
    @parameterized.expand([
        "google",
        "abc"
    ])
    @patch("client.get_json")
    def test_org(self, org: str, mock_get_json: MagicMock):
        """ Tests output for GithubOrgClient.org
        """
        mock_get_json.return_value = {}

        client = GithubOrgClient(org)
        self.assertEqual(client.org, {})
        mock_get_json.assert_called_once_with(client.ORG_URL.format(org=org))

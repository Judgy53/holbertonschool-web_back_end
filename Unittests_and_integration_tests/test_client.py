#!/usr/bin/env python3
""" Unit tests for client module
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
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

    def test_public_repos_url(self):
        """ Tests output for GithubOrgClient._public_repos_url
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "http://google.repos"}

            client = GithubOrgClient("google")
            self.assertEqual(client._public_repos_url, "http://google.repos")

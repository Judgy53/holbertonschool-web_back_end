#!/usr/bin/env python3
""" Unit tests for client module
"""
from typing import Dict
import unittest
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json: MagicMock):
        """ Tests output for GithubOrgClient.public_repos
        """
        mock_get_json.return_value = [
            {
                "name": "1st repo",
                "url": "http://google.repos/repo1"
            },
            {
                "name": "2nd repo",
                "url": "http://google.repos/repo2"
            }
        ]
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "http://google.repos/"

            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(), ["1st repo", "2nd repo"])
            mock_url.assert_called_once_with()
            mock_get_json.assert_called_once_with(mock_url.return_value)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, license_key: str, expected: bool):
        """ Tests output for GithubOrgClient.has_license()
        """
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class(("org_payload",
                      "repos_payload",
                      "expected_repos",
                      "apache2_repos"), TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test class for GithubOrgClient.public_repos
    """
    @classmethod
    def setUpClass(cls):
        """ Setup the mocks and the patcher
        """
        mock_repos = Mock()
        mock_repos.json.return_value = cls.repos_payload
        url_map = {cls.org_payload["repos_url"]: mock_repos}

        mock_org = Mock()
        mock_org.json.return_value = cls.org_payload

        cls.get_patcher = patch("requests.get")
        cls.get_patcher.start().side_effect = lambda url: url_map.get(url,
                                                                      mock_org)

    @classmethod
    def tearDownClass(cls):
        """ Stop the patcher
        """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test output of GithubOrgClient.public_repos
        """
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("WRONG_LICENSE"), [])

    def test_public_repos_with_license(self):
        """ Test output of GithubOrgClient.public_repos with license
        """
        client = GithubOrgClient("test_org")
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)

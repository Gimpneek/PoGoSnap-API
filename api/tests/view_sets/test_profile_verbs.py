""" Test the HTTP Verbs of profile """
import allure
from django.test import TestCase
from rest_framework.test import APIClient
from api.tests.common.test_data import create_profile, USER_NAME


class TestProfileVerbsCommon(TestCase):
    """
    Common setUp for Profile verb tests
    """

    def setUp(self):
        """ Set up the tests """
        super(TestProfileVerbsCommon, self).setUp()
        self.profile = create_profile()
        self.api = APIClient()
        self.api.login(
            username=USER_NAME,
            password=USER_NAME)
        self.url = '/api/v1/profiles/'


class TestProfileCollectionVerbs(TestProfileVerbsCommon):
    """
    Test the HTTP Verb access of Profile Collection
    """

    def test_not_logged_in(self):
        """
        Test that when user isn't authenticated read is allowed
        """
        self.api.logout()
        resp = self.api.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_get_allowed(self):
        """
        Test that get requests are allowed
        """
        resp = self.api.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_post_blocked(self):
        """
        Test that post requests are not allowed
        """
        resp = self.api.post(
            self.url,
            {
                'user': 1,
                'name': 'test',
                'location': 'test',
                'silph_card': 'test'
            },
            format='json')
        self.assertEqual(resp.status_code, 405)

    def test_delete_blocked(self):
        """
        Test that delete requests are not allowed
        """
        resp = self.api.delete(self.url)
        self.assertEqual(resp.status_code, 405)

    def test_put_blocked(self):
        """
        Test that the PUT verb is not allowed
        """
        resp = self.api.put(
            self.url,
            {
                'user': 1,
                'name': 'test',
                'location': 'test',
                'silph_card': 'test'
            },
            format='json'
        )
        self.assertEqual(resp.status_code, 405)


@allure.issue('https://wrensoftware.atlassian.net/browse/GOS-37')
@allure.story('View Player Profile')
class TestProfileResourceVerbs(TestProfileVerbsCommon):
    """ Test the HTTP Verb access of Profile Resource """

    def setUp(self):
        """ Setup the tests """
        super(TestProfileResourceVerbs, self).setUp()
        self.url = '/api/v1/profiles/1/'

    def test_not_logged_in(self):
        """
        Test that when user isn't authenticated read is allowed
        """
        self.api.logout()
        resp = self.api.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_get_allowed(self):
        """
        Test that get requests are allowed
        """
        resp = self.api.get(self.url)
        self.assertEqual(resp.status_code, 200)

    def test_post_blocked(self):
        """
        Test that post requests are not allowed
        """
        resp = self.api.post(
            self.url,
            {
                'user': 1,
                'name': 'test',
                'location': 'test',
                'silph_card': 'test'
            },
            format='json')
        self.assertEqual(resp.status_code, 405)

    def test_delete_blocked(self):
        """
        Test that delete requests are not allowed
        """
        resp = self.api.delete(self.url)
        self.assertEqual(resp.status_code, 405)

    def test_put_blocked(self):
        """
        Test that the PUT verb is not allowed
        """
        resp = self.api.put(
            self.url,
            {
                'user': 1,
                'name': 'test',
                'location': 'test',
                'silph_card': 'test'
            },
            format='json'
        )
        self.assertEqual(resp.status_code, 405)

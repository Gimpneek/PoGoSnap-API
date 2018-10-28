""" Test the HTTP Verbs of /me """
from django.test import TestCase
from rest_framework.test import APIClient
from api.tests.common.test_data import create_profile, USER_NAME


class TestMeVerbsCommon(TestCase):
    """
    Common setUp for Profile verb tests
    """

    def setUp(self):
        """ Set up the tests """
        super(TestMeVerbsCommon, self).setUp()
        self.profile = create_profile()
        self.api = APIClient()
        self.api.login(
            username=USER_NAME,
            password=USER_NAME)
        self.url = '/api/v1/profiles/me/'


class TestMeVerbs(TestMeVerbsCommon):
    """
    Test the HTTP Verb access of Profile Collection
    """

    def test_get_unauth(self):
        """
        Test that when user isn't authenticated read is allowed
        """
        self.api.logout()
        resp = self.api.get(self.url)
        self.assertEqual(resp.status_code, 401)

    def test_get_allowed(self):
        """
        Test that get requests are allowed
        """
        self.api.force_authenticate(user=self.profile.user)
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

    def test_post_unauth(self):
        """
        Test that post is blocked when unauthorised
        """
        self.api.logout()
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

    def test_delete_unauth(self):
        """
        Test that delete requests are blocked when unauthorised
        """
        self.api.logout()
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

    def test_put_unauth(self):
        """
        Test that PUT is blocked when unauthorised
        """
        self.api.logout()
        resp = self.api.put(
            self.url,
            {
                'user': 1,
                'name': 'test',
                'location': 'test',
                'silph_card': 'test'
            },
            format='json')
        self.assertEqual(resp.status_code, 405)

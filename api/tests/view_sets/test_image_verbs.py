""" Test the HTTP Verbs of Image """
import allure
from django.test import TestCase
from django.core.files import File
from unittest.mock import MagicMock
from rest_framework.test import APIClient
from api.tests.common.test_data import create_profile, create_pokemon, \
    create_image, create_access_token


class TestImageVerbsCommon(TestCase):
    """
    Common setUp for Image Verb Tests
    """

    def setUp(self):
        """ Set up the tests """
        super(TestImageVerbsCommon, self).setUp()
        self.pokemon = create_pokemon()
        self.profile = create_profile()
        self.image = create_image(pokemon=self.pokemon, profile=self.profile)
        self.access_token = create_access_token(user=self.profile.user)
        self.api = APIClient()
        self.url = '/api/v1/images/'


@allure.issue('https://wrensoftware.atlassian.net/browse/GOS-26')
@allure.story('See list of pokemon pictures')
class TestImageCollectionVerbs(TestImageVerbsCommon):
    """
    Test the HTTP Verb access of Image Collection
    """

    def test_get_unauth(self):
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

    def test_post_allowed(self):
        """
        Test that post requests are allowed
        """
        file_mock = MagicMock(spec=File, name='FileMock')
        file_mock.name = 'test.jpg'
        resp = self.api.post(
            self.url,
            {
                'pokemon': self.pokemon.id,
                'image': file_mock
            },
            format='multipart',
            HTTP_AUTHORIZATION='Bearer {0}'.format(self.access_token)
        )
        self.assertEqual(resp.status_code, 201)

    def test_post_error(self):
        """
        Test that when sending POST data that's bad it returns the correct
        error code
        """
        resp = self.api.post(
            self.url,
            {
                'pokemon': 'a'
            },
            format='json',
            HTTP_AUTHORIZATION='Bearer {0}'.format(self.access_token)
        )
        self.assertEqual(resp.status_code, 400)

    def test_post_unauth(self):
        """
        Test that when sending to POST when not logged in returns an error
        """
        self.api.logout()
        resp = self.api.post(
            self.url,
            {
                'pokemon': self.pokemon.id,
                'url': 'http://meh.jpg'
            },
            format='json')
        self.assertEqual(resp.status_code, 401)

    def test_delete_blocked(self):
        """
        Test that delete requests are not allowed
        """
        resp = self.api.delete(self.url)
        self.assertEqual(resp.status_code, 405)

    def test_delete_unauth(self):
        """
        Test that DELETE is blocked when not authorised
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
                'pokemon': self.pokemon.id,
                'url': 'http://meh.jpg'
            },
            format='json'
        )
        self.assertEqual(resp.status_code, 405)

    def test_put_unauth(self):
        """
        Test that PUT is blocked when not authorised
        """
        self.api.logout()
        resp = self.api.put(
            self.url,
            {
                'pokemon': self.pokemon.id,
                'url': 'http://meh.jpg'
            },
            format='json'
        )
        self.assertEqual(resp.status_code, 405)


@allure.issue('https://wrensoftware.atlassian.net/browse/GOS-29')
@allure.story('View Image')
class TestImageResourceVerbs(TestImageVerbsCommon):
    """ Test the HTTP Verb access of Image Resource """

    def setUp(self):
        """ Setup the tests """
        super(TestImageResourceVerbs, self).setUp()
        self.url = '/api/v1/profiles/{0}/'.format(self.profile.name)

    def test_get_unauth(self):
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
                'pokemon': self.pokemon.id,
                'url': 'http://meh.jpg'
            },
            format='json')
        self.assertEqual(resp.status_code, 405)

    def test_post_unauth(self):
        """
        Test that post request is blocked when not auth
        """
        self.api.logout()
        resp = self.api.post(
            self.url,
            {
                'pokemon': self.pokemon.id,
                'url': 'http://meh.jpg'
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
        Test that delete is blocked when not authorised
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
                'pokemon': self.pokemon.id,
                'url': 'http://meh.jpg'
            },
            format='json'
        )
        self.assertEqual(resp.status_code, 405)

    def test_put_unauth(self):
        """
        Test that PUT is blocked when not authorised
        """
        self.api.logout()
        resp = self.api.put(
            self.url,
            {
                'pokemon': self.pokemon.id,
                'url': 'http://meh.jpg'
            },
            format='json')
        self.assertEqual(resp.status_code, 405)

""" Test the HTTP Verbs of Image """
import allure
from django.test import TestCase
from rest_framework.test import APIClient
from api.tests.common.test_data import create_profile, create_pokemon, \
    create_image, USER_NAME


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
        self.api = APIClient()
        self.api.login(
            username=USER_NAME,
            password=USER_NAME)
        self.url = '/api/v1/images/'


@allure.issue('https://wrensoftware.atlassian.net/browse/GOS-26')
@allure.story('See list of pokemon pictures')
class TestImageCollectionVerbs(TestImageVerbsCommon):
    """
    Test the HTTP Verb access of Image Collection
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

    def test_post_allowed(self):
        """
        Test that post requests are allowed
        """
        resp = self.api.post(
            self.url,
            {
                'pokemon': self.pokemon.id,
                'url': 'http://meh.jpg'
            },
            format='json')
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
            format='json'
        )
        self.assertEqual(resp.status_code, 400)

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

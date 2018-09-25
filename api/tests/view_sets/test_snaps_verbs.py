""" Test the HTTP Verbs of Pokedex """
import allure
from django.test import TestCase
from rest_framework.test import APIClient
from api.tests.common.test_data import create_profile, create_pokemon, \
    create_image, create_collection, create_collection_entry, USER_NAME, \
    create_another_profile, ANOTHER_PROFILE_NAME


class TestSnapsVerbsCommon(TestCase):
    """
    Common setUp for Collection Verb Tests
    """

    def setUp(self):
        """ Set up the tests """
        super(TestSnapsVerbsCommon, self).setUp()
        self.profile = create_profile()
        self.pokemon = create_pokemon()
        self.image = create_image(profile=self.profile, pokemon=self.pokemon)
        self.entry = \
            create_collection_entry(image=self.image)
        self.pokedex = \
            create_collection(profile=self.profile, entries=[self.entry])
        self.api = APIClient()
        self.api.login(
            username=USER_NAME,
            password=USER_NAME)
        self.url = '/api/v1/profiles/{0}/images/'.format(self.profile.name)


@allure.story('User\'s Collection')
class TestSnapsCollectionVerbs(TestSnapsVerbsCommon):
    """
    Test the HTTP Verb access of User's Snaps
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

    def test_post_not_allowed(self):
        """
        Test that post requests are not allowed
        """
        resp = self.api.post(
            self.url,
            {
                'pokemon': self.pokemon.id,
                'profile': self.profile.id
            },
            format='json')
        self.assertEqual(resp.status_code, 405)

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
        self.assertEqual(resp.status_code, 405)

    def test_post_other_user(self):
        """
        Test that post to another User's image list is not allowed
        """
        create_another_profile()
        resp = self.api.post(
            '/api/v1/profiles/{0}/images/'.format(ANOTHER_PROFILE_NAME),
            {
                'pokemon': self.pokemon.id,
                'profile': self.profile.id
            },
            format='json')
        self.assertEqual(resp.status_code, 405)

    def test_post_unauth(self):
        """
        Test that post isn't allowed when unauthorised
        """
        self.api.logout()
        resp = self.api.post(
            self.url,
            {
                'pokemon': self.pokemon.id,
                'profile': self.profile.id
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
        Test that delete is blocked when unauthorised
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
        Test that PUT is blocked when unauthorised
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

""" Test the HTTP Verbs of Pokedex """
import allure
from django.test import TestCase
from rest_framework.test import APIClient
from api.tests.common.test_data import create_profile, create_pokemon, \
    create_image, create_collection, create_pokedex_entry, \
    create_another_profile, ANOTHER_PROFILE_NAME, create_access_token


class TestCollectionVerbsCommon(TestCase):
    """
    Common setUp for Collection Verb Tests
    """

    def setUp(self):
        """ Set up the tests """
        super(TestCollectionVerbsCommon, self).setUp()
        self.profile = create_profile()
        self.pokemon = create_pokemon()
        self.image = create_image(profile=self.profile, pokemon=self.pokemon)
        self.entry = \
            create_pokedex_entry(image=self.image)
        self.pokedex = \
            create_collection(profile=self.profile, entries=[self.entry])
        self.access_token = create_access_token(user=self.profile.user)
        self.api = APIClient()
        self.url = \
            '/api/v1/profiles/{0}/collections/'.format(self.profile.name)


@allure.story('User\'s Collection')
class TestCollectionsCollectionVerbs(TestCollectionVerbsCommon):
    """
    Test the HTTP Verb access of Collections Collection
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
        resp = self.api.post(
            self.url,
            {
                'name': 'Test Collection'
            },
            HTTP_AUTHORIZATION='Bearer {0}'.format(self.access_token),
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
            },
            HTTP_AUTHORIZATION='Bearer {0}'.format(self.access_token),
            format='json'
        )
        self.assertEqual(resp.status_code, 400)

    def test_post_other_user(self):
        """
        Test that post to another User's collections is not allowed
        """
        create_another_profile()
        resp = self.api.post(
            '/api/v1/profiles/{0}/collections/'.format(ANOTHER_PROFILE_NAME),
            {
                'name': 'Test Collection'
            },
            HTTP_AUTHORIZATION='Bearer {0}'.format(self.access_token),
            format='json')
        self.assertEqual(resp.status_code, 403)

    def test_post_unauth(self):
        """
        Test that post isn't allowed when unauthorised
        """
        self.api.logout()
        resp = self.api.post(
            self.url,
            {
                'name': 'Test Collection'
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
                'name': 'Test Collection'
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
                'name': 'Test Collection'
            },
            format='json')
        self.assertEqual(resp.status_code, 405)


class TestCollectionResourceVerbs(TestCollectionVerbsCommon):
    """ Test the HTTP Verb access of Image Resource """

    def setUp(self):
        """ Setup the tests """
        super(TestCollectionResourceVerbs, self).setUp()
        self.url = \
            '/api/v1/profiles/{profile_id}/collections/{collection_id}/'\
            .format(
                profile_id=self.profile.name,
                collection_id=self.pokedex.id
            )

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
        Test that post requests are allowed
        """
        resp = self.api.post(
            self.url,
            {
                'name': 'Test Pokedex'
            },
            HTTP_AUTHORIZATION='Bearer {0}'.format(self.access_token),
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
                'name': 'Test Pokedex'
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
                'name': 'Test Pokedex'
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
                'name': 'Test Pokedex'
            },
            format='json')
        self.assertEqual(resp.status_code, 405)

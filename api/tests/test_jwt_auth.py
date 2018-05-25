""" Tests for JSON Web Token endpoint """
from django.test import TestCase
from api.tests.common.test_data import create_profile, USER_NAME, \
    create_pokemon, create_image, create_pokedex_entry, create_pokedex


class TestJwtAuth(TestCase):
    """
    Test that the django rest framework JWT auth works
    """

    def setUp(self):
        """
        Set up tests
        """
        super(TestJwtAuth, self).setUp()
        self.profile = create_profile()
        self.pokemon = create_pokemon()
        self.image = create_image(profile=self.profile, pokemon=self.pokemon)
        self.entry = \
            create_pokedex_entry(image=self.image, pokemon=self.pokemon)
        self.pokedex = \
            create_pokedex(profile=self.profile, entries=[self.entry])
        self.url = '/api/v1/profiles/{0}/pokedex/'.format(self.profile.name)

    def test_unauthed(self):
        """
        Test that with no authorisation we get a 401 back
        """
        resp = self.client.post(
            self.url,
            {
                'pokemon': self.pokemon.id,
                'url': 'http://meh.jpg'
            },
            format='json')
        self.assertEqual(resp.status_code, 401)

    def test_get_token(self):
        """
        Test that hitting up token endpoint returns token
        """
        resp = self.client.post(
            '/api/v1/api-token-auth/',
            {
                'username': USER_NAME,
                'password': USER_NAME
            },
            follow=True
        )
        self.assertEqual(resp.status_code, 200)
        self.assertTrue('token' in resp.json().keys())

    def test_bad_creds(self):
        """
        Test trying to get a token with bad credentials returns an error
        """
        resp = self.client.post(
            '/api/v1/api-token-auth/',
            {
                'username': 'test123',
                'password': 'password'
            },
            follow=True
        )
        self.assertEqual(resp.status_code, 400)
        self.assertTrue('non_field_errors' in resp.json().keys())

    def test_authed_access(self):
        """
        Test that hitting up token endpoint returns token
        """
        resp = self.client.post(
            '/api/v1/api-token-auth/',
            {
                'username': USER_NAME,
                'password': USER_NAME
            }
        )
        token = resp.json().get('token')
        self.assertEqual(resp.status_code, 200)
        authed_resp = self.client.post(
            self.url,
            {
                'pokemon': self.pokemon.id,
                'image': self.image.id
            },
            HTTP_AUTHORIZATION='Bearer {}'.format(token),
            format='json')
        self.assertEqual(authed_resp.status_code, 201)

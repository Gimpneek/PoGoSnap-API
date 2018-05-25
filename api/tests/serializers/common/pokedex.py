""" Common set up for testing Pokedex API """
from django.test import TestCase
from api.tests.common.test_data import PROFILE_NAME


class PokedexSerializerCase(TestCase):
    """
    Common setup for testing the Pokedex API endpoints
    """

    def setUp(self):
        """ Set up the tests """
        super(PokedexSerializerCase, self).setUp()
        self.url = '/api/v1/profiles/{0}/pokedex/'.format(PROFILE_NAME)

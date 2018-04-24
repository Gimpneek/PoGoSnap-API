""" Common set up for testing Profile API """
from django.test import TestCase


class ProfileSerializerCase(TestCase):
    """
    Common setup for testing the Profile API endpoints
    """

    def setUp(self):
        """ Set up the tests """
        super(ProfileSerializerCase, self).setUp()
        self.url = '/api/v1/profile/'

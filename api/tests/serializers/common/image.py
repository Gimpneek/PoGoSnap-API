""" Common set up for testing Image API """
from django.test import TestCase


class ImageSerializerCase(TestCase):
    """
    Common setup for testing the Image API endpoints
    """

    def setUp(self):
        """ Set up the tests """
        super(ImageSerializerCase, self).setUp()
        self.url = '/api/v1/images/'

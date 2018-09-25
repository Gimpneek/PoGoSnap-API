""" Common set up for testing Collection API """
from django.test import TestCase
from api.tests.common.test_data import PROFILE_NAME


class CollectionEntrySerializerCase(TestCase):
    """
    Common setup for testing the Collection API endpoints
    """

    def setUp(self):
        """ Set up the tests """
        super(CollectionEntrySerializerCase, self).setUp()
        self.url = '/api/v1/profiles/{0}/collections/{1}/entries/'\
            .format(PROFILE_NAME, 1)

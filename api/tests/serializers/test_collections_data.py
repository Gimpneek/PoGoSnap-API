""" Test the API for Pokedex """
import allure
from rest_framework.test import APIClient
from api.tests.serializers.common.collection import CollectionSerializerCase
from api.tests.common.test_data import create_image, create_profile, \
    create_pokemon, create_collection_entry, create_collection


@allure.story('User\'s Collection')
class TestCollectionsCollectionData(CollectionSerializerCase):
    """
    Test the Pokedex collection endpoints data structure
    """

    def setUp(self):
        """ Set up the test """
        super(TestCollectionsCollectionData, self).setUp()
        self.profile = create_profile()
        self.pokemon = create_pokemon()
        self.image = create_image(profile=self.profile, pokemon=self.pokemon)
        self.entry = \
            create_collection_entry(image=self.image)
        self.pokedex = \
            create_collection(profile=self.profile, entries=[self.entry])
        self.api = APIClient()
        resp = self.api.get(self.url)
        self.result = resp.data.get('results')[0]

    def test_id(self):
        """
        Test that the id of the collection is returned
        """
        self.assertEqual(self.result.get('id'), self.pokedex.id)

    def test_name(self):
        """
        Test that the name of the collection is returned
        """
        self.assertEqual(self.result.get('name'), 'Pokedex')

    def test_type(self):
        """
        Test that the type of the colletion is returned
        """
        self.assertEqual(self.result.get('type'), 'pokedex')


class TestCollectionsResourceData(CollectionSerializerCase):
    """
    Test the Collection Resource endpoints data structure
    """

    def setUp(self):
        """ Set up the test """
        super(TestCollectionsResourceData, self).setUp()
        self.profile = create_profile()
        self.pokemon = create_pokemon()
        self.image = create_image(profile=self.profile, pokemon=self.pokemon)
        self.entry = \
            create_collection_entry(image=self.image)
        self.pokedex = \
            create_collection(profile=self.profile, entries=[self.entry])
        self.api = APIClient()
        self.resource_url = '{0}{1}/'.format(self.url, self.pokedex.id)
        resp = self.api.get(self.resource_url)
        self.result = resp.data

    def test_id(self):
        """
        Test the id of the collection is returned
        """
        self.assertEqual(self.result.get('id'), self.pokedex.id)

    def test_name(self):
        """
        Test the name of the collection is returned
        """
        self.assertEqual(self.result.get('name'), 'Pokedex')

    def test_type(self):
        """
        Test that the type of the collection is returned
        """
        self.assertEqual(self.result.get('type'), 'pokedex')

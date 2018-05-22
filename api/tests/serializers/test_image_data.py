""" Test the API for Image """
import allure
from rest_framework.test import APIClient
from api.tests.serializers.common.image import ImageSerializerCase
from api.tests.common.test_data import create_image, create_profile, \
    create_pokemon


@allure.issue('https://wrensoftware.atlassian.net/browse/GOS-26')
@allure.story('See list of pokemon pictures')
class TestImageCollectionData(ImageSerializerCase):
    """
    Test the Image collection endpoints data structure
    """

    def setUp(self):
        """ Set up the test """
        super(TestImageCollectionData, self).setUp()
        self.profile = create_profile()
        self.pokemon = create_pokemon()
        self.image = create_image(profile=self.profile, pokemon=self.pokemon)
        self.api = APIClient()
        resp = self.api.get(self.url)
        self.result = resp.data.get('results')[0]

    def test_collection_id(self):
        """
        Test the id property of the collection
        """
        self.assertEqual(self.result.get('id'), self.image.id)

    def test_collection_url(self):
        """
        Test the url property of the collection
        """
        self.assertEqual(self.result.get('image'), self.image.image.name)

    def test_collection_profile_id(self):
        """
        Test the profile id of the collection
        """
        self.assertEqual(self.result.get('profile').get('id'), self.profile.id)

    def test_collection_profile_name(self):
        """
        Test the profile name of the collection
        """
        self.assertEqual(
            self.result.get('profile').get('name'), self.profile.name)

    def test_collection_profile_loc(self):
        """
        Test the profile location of the collection
        """
        self.assertEqual(
            self.result.get('profile').get('location'), self.profile.location)

    def test_collection_profile_card(self):
        """
        Test the profile silph_card of the collection
        """
        self.assertEqual(
            self.result.get('profile').get('silph_card'),
            self.profile.silph_card
        )

    def test_collection_pokemon_id(self):
        """
        Test the pokemon id of the collection
        """
        self.assertEqual(
            self.result.get('pokemon').get('id'),
            self.pokemon.id
        )

    def test_collection_pokemon_name(self):
        """
        Test the pokemon name of the collection
        """
        self.assertEqual(
            self.result.get('pokemon').get('name'),
            self.pokemon.name
        )

    def test_collection_pokemon_dex(self):
        """
        Test the pokemon dex_number of the collection
        """
        self.assertEqual(
            self.result.get('pokemon').get('dex_number'),
            self.pokemon.dex_number
        )


@allure.issue('https://wrensoftware.atlassian.net/browse/GOS-29')
@allure.story('View Image')
class TestImageResourceData(ImageSerializerCase):
    """
    Test the Image resource endpoint data structure
    """

    def setUp(self):
        """
        Set up the test
        """
        super(TestImageResourceData, self).setUp()
        self.profile = create_profile()
        self.pokemon = create_pokemon()
        self.image = create_image(profile=self.profile, pokemon=self.pokemon)
        self.api = APIClient()
        resp = self.api.get(
            '{url}{id}/'.format(url=self.url, id=self.image.id))
        self.result = resp.data

    def test_resource_id(self):
        """
        Test the id property of the resource
        """
        self.assertEqual(self.result.get('id'), self.image.id)

    def test_resource_image(self):
        """
        Test the name property of the resource
        """
        self.assertEqual(self.result.get('image'), self.image.image.name)

    def test_resource_desc(self):
        """
        Test the description property of the resource
        """
        self.assertEqual(
            self.result.get('description'), self.image.description)

    def test_resource_profile_id(self):
        """
        Test the profile id of the resource
        """
        self.assertEqual(self.result.get('profile').get('id'), self.profile.id)

    def test_resource_profile_name(self):
        """
        Test the profile name of the resource
        """
        self.assertEqual(
            self.result.get('profile').get('name'), self.profile.name)

    def test_resource_profile_location(self):
        """
        Test the profile location of the resource
        """
        self.assertEqual(
            self.result.get('profile').get('location'), self.profile.location)

    def test_resource_profile_card(self):
        """
        Test the profile silph_card of the resource
        """
        self.assertEqual(
            self.result.get('profile').get('silph_card'),
            self.profile.silph_card
        )

    def test_resource_pokemon_id(self):
        """
        Test the pokemon id of the resource
        """
        self.assertEqual(
            self.result.get('pokemon').get('id'),
            self.pokemon.id
        )

    def test_resource_pokemon_name(self):
        """
        Test the pokemon name of the resource
        """
        self.assertEqual(
            self.result.get('pokemon').get('name'),
            self.pokemon.name
        )

    def test_resource_pokemon_dex(self):
        """
        Test the pokemon dex_number of the resource
        """
        self.assertEqual(
            self.result.get('pokemon').get('dex_number'),
            self.pokemon.dex_number
        )

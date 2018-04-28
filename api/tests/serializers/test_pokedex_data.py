""" Test the API for Pokedex """
from rest_framework.test import APIClient
from api.tests.serializers.common.pokedex import PokedexSerializerCase
from api.tests.common.test_data import create_image, create_profile, \
    create_pokemon, create_pokedex_entry, create_pokedex


class TestPokedexCollectionData(PokedexSerializerCase):
    """
    Test the Pokedex collection endpoints data structure
    """

    def setUp(self):
        """ Set up the test """
        super(TestPokedexCollectionData, self).setUp()
        self.profile = create_profile()
        self.pokemon = create_pokemon()
        self.image = create_image(profile=self.profile, pokemon=self.pokemon)
        self.entry = \
            create_pokedex_entry(image=self.image, pokemon=self.pokemon)
        self.pokedex = \
            create_pokedex(profile=self.profile, entries=[self.entry])
        self.api = APIClient()
        resp = self.api.get(self.url)
        self.result = resp.data.get('results')[0]

    def test_id(self):
        """
        Test the id property of the collection
        """
        self.assertEqual(self.result.get('id'), self.entry.id)

    def test_pokemon_id(self):
        """
        Test the pokemon.id property of the collection
        """
        self.assertEqual(
            self.result.get('pokemon').get('id'), self.entry.pokemon.id)

    def test_pokemon_name(self):
        """
        Test the pokemon.name property of the collection
        """
        self.assertEqual(
            self.result.get('pokemon').get('name'), self.entry.pokemon.name)

    def test_pokemon_dex(self):
        """
        Test the pokemon.dex_number property of the collection
        """
        self.assertEqual(
            self.result.get('pokemon').get('dex_number'),
            self.entry.pokemon.dex_number
        )

    def test_image_id(self):
        """
        Test the image.id property of the collection
        """
        self.assertEqual(self.result.get('image').get('id'), self.image.id)

    def test_image_url(self):
        """
        Test the image.url property of the collection
        """
        self.assertEqual(self.result.get('image').get('url'), self.image.url)

    def test_image_pkmn_id(self):
        """
        Test the image.pokemon.id property of the collection
        """
        self.assertEqual(
            self.result.get('image').get('pokemon').get('id'),
            self.image.pokemon.id
        )

    def test_image_pkmn_name(self):
        """
        Test the image.pokemon.name property of the collection
        """
        self.assertEqual(
            self.result.get('image').get('pokemon').get('name'),
            self.image.pokemon.name
        )

    def test_image_pkmn_dex(self):
        """
        Test the image.pokemon.dex_number property of the collection
        """
        self.assertEqual(
            self.result.get('image').get('pokemon').get('dex_number'),
            self.image.pokemon.dex_number
        )

    def test_image_profile_id(self):
        """
        Test the image.profile.id property of the collection
        """
        self.assertEqual(
            self.result.get('image').get('profile').get('id'),
            self.image.profile.id
        )

    def test_image_profile_name(self):
        """
        Test the image.profile.name property of the collection
        """
        self.assertEqual(
            self.result.get('image').get('profile').get('name'),
            self.image.profile.name
        )

    def test_image_profile_loc(self):
        """
        Test the image.profile.location property of the collection
        """
        self.assertEqual(
            self.result.get('image').get('profile').get('location'),
            self.image.profile.location
        )

    def test_image_profile_card(self):
        """
        Test the image.profile.silph_card property of the collection
        """
        self.assertEqual(
            self.result.get('image').get('profile').get('silph_card'),
            self.image.profile.silph_card
        )

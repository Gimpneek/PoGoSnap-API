""" Tests for Pokedex Entry Model """
from django.test import TestCase
from api.models.pokedex_entry import PokedexEntry
from api.tests.common.test_data import create_pokemon, create_image, \
    create_pokedex, create_profile


class TestPokedexEntryObject(TestCase):
    """ Test the creation of the Pokedex Entry Object """

    def setUp(self):
        """ Set up the tests """
        self.profile = create_profile()
        self.image = create_image()
        self.pokemon = create_pokemon()
        self.pokedex_entry = PokedexEntry.objects.create(
            image=self.image,
            pokemon=self.pokemon
        )
        self.pokedex = create_pokedex(self.profile, [self.pokedex_entry])

    def test_image(self):
        """
        Test that the image that's passed in creation is saved to the object
        correctly
        """
        self.assertEqual(self.pokedex_entry.image.id, self.image.id)

    def test_pokemon(self):
        """
        Test that the pokemon that's passed in creation is saved to the object
        correctly
        """
        self.assertEqual(self.pokedex_entry.pokemon.id, self.pokemon.id)

    def test_string_rep(self):
        """
        Test the string representation of the object
        """
        self.assertEqual(
            str(self.pokedex_entry),
            "{0} image in {1}'s Pokedex".format(self.pokemon, self.profile)
        )

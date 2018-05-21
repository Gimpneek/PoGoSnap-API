""" Tests for Pokemon Model """
from django.test import TestCase
from api.models.pokemon import Pokemon
from api.tests.common.test_data import POKEMON_NAME, POKEMON_NUMBER


class TestPokemonObject(TestCase):
    """ Test the creation of the Pokemon Object """

    def setUp(self):
        super(TestPokemonObject, self).setUp()
        self.pokemon = Pokemon.objects.create(
            name=POKEMON_NAME,
            dex_number=POKEMON_NUMBER
        )

    def test_name(self):
        """
        Test the name passed on creation is saved on the object
        """
        self.assertEqual(self.pokemon.name, POKEMON_NAME)

    def test_dex_number(self):
        """
        Test the dex number passed on creation is saved on the object
        """
        self.assertEqual(self.pokemon.dex_number, POKEMON_NUMBER)

    def test_string_rep(self):
        """
        Test the string representation of the object
        """
        self.assertEqual(
            str(self.pokemon),
            "{0}(#{1})".format(POKEMON_NAME, POKEMON_NUMBER)
        )

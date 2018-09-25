""" Tests for Pokedex Model """
from django.test import TestCase
from api.models.pokedex import Pokedex
from api.tests.common.test_data import create_pokedex_entry, create_profile


class TestPokedexObject(TestCase):
    """ Test the creation of the Pokedex Object """

    def setUp(self):
        """
        Set up tests
        """
        super(TestPokedexObject, self).setUp()
        self.profile = create_profile()
        self.pokedex_entry = create_pokedex_entry()
        self.pokedex = Pokedex.objects.create(name='Pokedex')
        self.pokedex.profile.add(self.profile)
        self.pokedex.entries.add(self.pokedex_entry)
        self.pokedex.save()

    def test_profile(self):
        """
        Test that the profile passed on creation is saved to the object
        """
        self.assertEqual(self.pokedex.profile.all()[0].id, self.profile.id)

    def test_entries(self):
        """
        Test that assigning a pokedex entry to the pokedex is saved
        """
        self.assertEqual(
            self.pokedex.entries.all()[0].id, self.pokedex_entry.id)

    def test_string_rep(self):
        """
        Test the string representation of the object
        """
        self.assertEqual(
            str(self.pokedex),
            "{0}'s Pokedex".format(self.profile)
        )

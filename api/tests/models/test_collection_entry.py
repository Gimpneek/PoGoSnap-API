""" Tests for Pokedex Entry Model """
from django.test import TestCase
from datetime import datetime
from api.models.collection_entry import CollectionEntry
from api.tests.common.test_data import create_pokemon, create_image, \
    create_collection, create_profile


class TestCollectionEntryObject(TestCase):
    """ Test the creation of the Collection Entry Object """

    def setUp(self):
        """ Set up the tests """
        self.profile = create_profile()
        self.image = create_image()
        self.pokemon = create_pokemon()
        self.pokedex_entry = CollectionEntry.objects.create(
            image=self.image
        )
        self.pokedex = create_collection(self.profile, [self.pokedex_entry])
        self.nowish = datetime.now()

    def test_image(self):
        """
        Test that the image that's passed in creation is saved to the object
        correctly
        """
        self.assertEqual(self.pokedex_entry.image.id, self.image.id)

    def test_create_date_year(self):
        """
        Test the create_date passed is saved to the object
        """
        self.assertEqual(self.pokedex_entry.create_date.year, self.nowish.year)

    def test_create_date_month(self):
        """
        Test the create_date passed is saved to the object
        """
        self.assertEqual(
            self.pokedex_entry.create_date.month,
            self.nowish.month
        )

    def test_create_date_day(self):
        """
        Test the create_date passed is saved to the object
        """
        self.assertEqual(self.pokedex_entry.create_date.day, self.nowish.day)

    def test_create_date_hour(self):
        """
        Test the create_date passed is saved to the object
        """
        self.assertEqual(self.pokedex_entry.create_date.hour, self.nowish.hour)

    def test_string_rep(self):
        """
        Test the string representation of the object
        """
        self.assertEqual(
            str(self.pokedex_entry),
            "{0} image in {1}'s Pokedex".format(
                self.image.pokemon.name,
                self.profile
            )
        )

""" Tests for Image Model """
from django.test import TestCase
from api.models.image import Image
from api.tests.common.test_data import create_pokemon, create_profile, \
    IMAGE_URL


class TestImageObject(TestCase):
    """ Test the creation of the Image Object """

    def setUp(self):
        super(TestImageObject, self).setUp()
        self.pokemon = create_pokemon()
        self.profile = create_profile()
        self.image = Image.objects.create(
            url=IMAGE_URL,
            pokemon=self.pokemon,
            profile=self.profile
        )

    def test_url(self):
        """
        Test the URL passed is saved to the object
        """
        self.assertEqual(self.image.url, IMAGE_URL)

    def test_pokemon(self):
        """
        Test the Pokemon passed is saved to the object
        """
        self.assertEqual(self.image.pokemon.id, self.pokemon.id)

    def test_profile(self):
        """
        Test the Profile passed is saved to the object
        """
        self.assertEqual(self.image.profile.id, self.profile.id)

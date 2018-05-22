""" Tests for Image Model """
from django.test import TestCase
from api.models.image import Image
from api.tests.common.test_data import create_pokemon, create_profile, \
    IMAGE_URL, IMAGE_DESC


class TestImageObject(TestCase):
    """ Test the creation of the Image Object """

    def setUp(self):
        super(TestImageObject, self).setUp()
        self.pokemon = create_pokemon()
        self.profile = create_profile()
        self.image = Image.objects.create(
            image=IMAGE_URL,
            pokemon=self.pokemon,
            profile=self.profile,
            description=IMAGE_DESC
        )

    def test_image(self):
        """
        Test the URL passed is saved to the object
        """
        self.assertEqual(self.image.image.name, IMAGE_URL)

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

    def test_description(self):
        """
        Test the description passed is save to the object
        """
        self.assertEqual(self.image.description, IMAGE_DESC)

    def test_string_rep(self):
        """
        Test the string representation of the object
        """
        self.assertEqual(
            str(self.image),
            "Picture of {0} by {1}".format(self.pokemon, self.profile)
        )

""" Tests for Profile Model """
from datetime import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from api.models.profile import Profile
from api.tests.common.test_data import USER_NAME, PROFILE_NAME, \
    PROFILE_LOCATION, PROFILE_SILPH_CARD_URL, create_image


class TestProfileObject(TestCase):
    """ Test the profile object """

    def setUp(self):
        """ Set up the tests """
        super(TestProfileObject, self).setUp()
        self.user = User.objects.create(username=USER_NAME)
        self.profile = Profile.objects.create(
            user=self.user,
            name=PROFILE_NAME,
            location=PROFILE_LOCATION,
            silph_card=PROFILE_SILPH_CARD_URL
        )
        self.image = create_image(profile=self.profile)
        self.profile.featured_image = self.image
        self.profile.save()
        self.nowish = datetime.now()

    def test_user(self):
        """
        Test that the user passed on creation is saved to the object
        """
        self.assertEqual(self.profile.user.id, self.user.id)

    def test_name(self):
        """
        Test that name passed on creation is saved to the object
        """
        self.assertEqual(self.profile.name, PROFILE_NAME)

    def test_location(self):
        """
        Test that location passed on creation is saved to the object
        """
        self.assertEqual(self.profile.location, PROFILE_LOCATION)

    def test_silph_card(self):
        """
        Test that silph card passed on creation is saved to the object
        """
        self.assertEqual(self.profile.silph_card, PROFILE_SILPH_CARD_URL)

    def test_featured_image(self):
        """
        Test that featured_image saved to profile is saved to the object
        """
        self.assertEqual(self.profile.featured_image, self.image)

    def test_create_date_year(self):
        """
        Test the create_date passed is saved to the object
        """
        self.assertEqual(self.profile.create_date.year, self.nowish.year)

    def test_create_date_month(self):
        """
        Test the create_date passed is saved to the object
        """
        self.assertEqual(self.profile.create_date.month, self.nowish.month)

    def test_create_date_day(self):
        """
        Test the create_date passed is saved to the object
        """
        self.assertEqual(self.profile.create_date.day, self.nowish.day)

    def test_create_date_hour(self):
        """
        Test the create_date passed is saved to the object
        """
        self.assertEqual(self.profile.create_date.hour, self.nowish.hour)

    def test_string_rep(self):
        """
        Test the string representation of the object
        """
        self.assertEqual(
            str(self.profile),
            "{0}".format(PROFILE_NAME)
        )

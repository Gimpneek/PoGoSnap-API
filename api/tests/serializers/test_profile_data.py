""" Test the API for Profile """
import allure
from rest_framework.test import APIClient
from api.tests.serializers.common.profile import ProfileSerializerCase
from api.tests.common.test_data import create_profile, create_image


class TestProfileCollectionData(ProfileSerializerCase):
    """
    Test the profile collection endpoints data structure
    """

    def setUp(self):
        """ Set up the test """
        super(TestProfileCollectionData, self).setUp()
        self.profile = create_profile()
        self.image = create_image(profile=self.profile)
        self.profile.featured_image = self.image
        self.profile.save()
        self.api = APIClient()
        resp = self.api.get(self.url)
        self.result = resp.data.get('results')[0]

    def test_collection_id(self):
        """
        Test the id property of the profile data
        """
        self.assertEqual(self.result.get('id'), self.profile.id)

    def test_collection_name(self):
        """
        Test the name property of the profile endpoint
        """
        self.assertEqual(self.result.get('name'), self.profile.name)

    def test_collection_location(self):
        """
        Test the location property of the profile endpoint
        """
        self.assertEqual(self.result.get('location'), self.profile.location)

    def test_collection_card(self):
        """
        Test the card property of the profile endpoint
        """
        self.assertEqual(
            self.result.get('silph_card'), self.profile.silph_card)

    def test_collection_image(self):
        """
        Test the featured_image property of the profile endpoint
        """
        self.assertEqual(
            self.result.get('image'),
            self.profile.featured_image.image)


@allure.issue('https://wrensoftware.atlassian.net/browse/GOS-37')
@allure.story('View Player Profile')
class TestProfileResourceData(ProfileSerializerCase):
    """
    Test the profile resource endpoint data structure
    """

    def setUp(self):
        """
        Set up the test
        """
        super(TestProfileResourceData, self).setUp()
        self.profile = create_profile()
        self.image = create_image(profile=self.profile)
        self.profile.featured_image = self.image
        self.profile.save()
        self.api = APIClient()
        resp = self.api.get(
            '{url}{id}/'.format(url=self.url, id=self.profile.name))
        self.result = resp.data

    def test_resource_id(self):
        """
        Test the id property of the resource
        """
        self.assertEqual(self.result.get('id'), self.profile.id)

    def test_resource_name(self):
        """
        Test the name property of the resource
        """
        self.assertEqual(self.result.get('name'), self.profile.name)

    def test_resource_location(self):
        """
        Test the location property of the resource
        """
        self.assertEqual(self.result.get('location'), self.profile.location)

    def test_resource_card(self):
        """
        test the silph_card property of the resource
        """
        self.assertEqual(
            self.result.get('silph_card'), self.profile.silph_card)

    def test_resource_image(self):
        """
        Test the featured_image property of the resource
        """
        self.assertEqual(
            self.profile.featured_image.image,
            self.result.get('image')
        )

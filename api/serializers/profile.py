# pylint: disable=no-self-use
""" Serializer for Profile model """
from rest_framework import serializers
from api.models.profile import Profile


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for Profile model """

    image = serializers.SerializerMethodField('get_featured_image')

    class Meta:
        """ Meta class for serializer """
        model = Profile
        fields = (
            'id',
            'name',
            'location',
            'silph_card',
            'image'
        )

    def get_featured_image(self, obj):
        """
        Get the featured image for the object (it will be under the image key)

        :param obj: Instance of profile model
        :return: featured_image field
        """
        if obj.featured_image:
            return obj.featured_image.image
        return ''

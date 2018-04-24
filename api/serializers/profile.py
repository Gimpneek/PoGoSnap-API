# pylint: disable=no-self-use
""" Serializer for Profile model """
from api.models.profile import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer for Profile model """

    class Meta:
        """ Meta class for serializer """
        model = Profile
        fields = (
            'id',
            'name',
            'location',
            'silph_card'
        )

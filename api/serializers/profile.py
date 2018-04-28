# pylint: disable=no-self-use
""" Serializer for Profile model """
from rest_framework import serializers
from api.models.profile import Profile


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

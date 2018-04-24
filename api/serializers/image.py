# pylint: disable=no-self-use
""" Serializer for Image model """
from api.models.image import Image
from api.serializers.profile import ProfileSerializer
from api.serializers.pokemon import PokemonSerializer
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    """ Serializer for Image model """

    profile = ProfileSerializer(read_only=True, many=False)
    pokemon = PokemonSerializer(read_only=True, many=False)

    class Meta:
        """ Meta class for serializer """
        model = Image
        fields = (
            'id',
            'url',
            'pokemon',
            'profile'
        )

# pylint: disable=no-self-use
""" Serializer for Collection model """
from rest_framework import serializers
from api.models.pokedex import Pokedex
from api.serializers.pokedex_entry import PokedexEntrySerializer


class CollectionSerializer(serializers.ModelSerializer):
    """ Serializer for Collection model """

    entries = PokedexEntrySerializer(many=True, read_only=True)

    class Meta:
        """ Meta class for serializer """
        model = Pokedex
        fields = (
            'id',
            'entries'
        )

# pylint: disable=no-self-use
""" Serializer for Pokemon model """
from rest_framework import serializers
from api.models.pokemon import Pokemon


class PokemonSerializer(serializers.ModelSerializer):
    """ Serializer for Pokemon model """

    class Meta:
        """ Meta class for serializer """
        model = Pokemon
        fields = (
            'id',
            'name',
            'dex_number'
        )

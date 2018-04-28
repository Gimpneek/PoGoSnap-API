# pylint: disable=no-self-use
""" Serializer for PokedexEntry model """
from rest_framework import serializers
from api.models.pokedex_entry import PokedexEntry
from api.serializers.pokemon import PokemonSerializer
from api.serializers.image import ImageSerializer


class PokedexEntrySerializer(serializers.ModelSerializer):
    """ Serializer for PokedexEntry model """

    pokemon = PokemonSerializer(many=False, read_only=True)
    image = ImageSerializer(many=False, read_only=True)

    class Meta:
        """ Meta class for serializer """
        model = PokedexEntry
        fields = (
            'id',
            'pokemon',
            'image'
        )

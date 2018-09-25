# pylint: disable=no-self-use
""" Serializer for CollectionEntry model """
from rest_framework import serializers
from api.models.collection_entry import CollectionEntry
from api.serializers.pokemon import PokemonSerializer
from api.serializers.image import ImageSerializer


class CollectionEntrySerializer(serializers.ModelSerializer):
    """ Serializer for CollectionEntry model """

    pokemon = PokemonSerializer(many=False, read_only=True)
    image = ImageSerializer(many=False, read_only=True)

    class Meta:
        """ Meta class for serializer """
        model = CollectionEntry
        fields = (
            'id',
            'pokemon',
            'image'
        )

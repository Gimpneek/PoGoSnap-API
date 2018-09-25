# pylint: disable=no-self-use
""" Serializer for CollectionEntry model """
from rest_framework import serializers
from api.models.collection_entry import CollectionEntry
from api.serializers.image import ImageSerializer


class CollectionEntrySerializer(serializers.ModelSerializer):
    """ Serializer for CollectionEntry model """

    image = ImageSerializer(many=False, read_only=True)

    class Meta:
        """ Meta class for serializer """
        model = CollectionEntry
        fields = (
            'id',
            'image'
        )

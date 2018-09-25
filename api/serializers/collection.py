# pylint: disable=no-self-use
""" Serializer for Collection model """
from rest_framework import serializers
from api.models.collection import Collection
from api.serializers.collection_entry import CollectionEntrySerializer


class CollectionSerializer(serializers.ModelSerializer):
    """ Serializer for Collection model """

    entries = CollectionEntrySerializer(many=True, read_only=True)

    class Meta:
        """ Meta class for serializer """
        model = Collection
        fields = (
            'id',
            'entries',
            'name',
            'type'
        )

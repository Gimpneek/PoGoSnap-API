# pylint: disable=no-self-use
""" Serializer for Collection model """
from rest_framework import serializers
from api.models.collection import Collection
from api.serializers.collection_entry import CollectionEntrySerializer


class CollectionSerializer(serializers.ModelSerializer):
    """ Serializer for Collection model """

    class Meta:
        """ Meta class for serializer """
        model = Collection
        fields = (
            'id',
            'name',
            'type'
        )

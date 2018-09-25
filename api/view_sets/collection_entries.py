# pylint: disable=too-many-ancestors
""" View Set for Collection Serializer """
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from api.models.profile import Profile
from api.models.collection import Collection
from api.models.collection_entry import CollectionEntry
from api.models.image import Image
from api.serializers.collection_entry import CollectionEntrySerializer
from api.forms.collection_entry import CollectionEntryForm


class CollectionEntriesViewSet(viewsets.GenericViewSet,
                               mixins.ListModelMixin,
                               mixins.CreateModelMixin):
    """
    View Set for Collection Entry Serializer
    """

    queryset = CollectionEntry.objects.all().order_by('id')
    serializer_class = CollectionEntrySerializer

    # pylint: disable=no-self-use,arguments-differ
    def create(self, request, profile_name=None, collections_pk=None):
        """
        Create a Collection

        :param request: Django Request
        :param profile_name: Name of the profile that holds the collection
        :param collections_pk: ID of the collection to add entry
        :return: Response code
        """
        if not request.user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        profile = Profile.objects.get(name__iexact=profile_name)
        collection = Collection.objects.get(pk=collections_pk)
        if request.user.id != profile.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        form = CollectionEntryForm(request.data)
        if form.is_valid():
            image = Image.objects.get(id=form.data.get('image'))
            collection_entry = CollectionEntry.objects.create(
                image=image
            )
            collection.entries.add(collection_entry)
            collection.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

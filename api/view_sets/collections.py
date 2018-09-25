# pylint: disable=too-many-ancestors
""" View Set for Collection Serializer """
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from api.models.profile import Profile
from api.models.pokedex import Pokedex
from api.serializers.collection import CollectionSerializer
from api.forms.collections import CollectionForm


class CollectionsViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin):
    """
    View Set for Collection Serializer
    """

    queryset = Pokedex.objects.all().order_by('id')
    serializer_class = CollectionSerializer

    # # pylint: disable=arguments-differ
    # def list(self, request, profile_name=None):
    #     """
    #     List the entries from the supplied Profile's pokedex
    #
    #     :param request: Django Request
    #     :param profile_name: Name of the profile to fetch PokedexEntries from
    #     :return: List of PokedexEntries
    #     """
    #     profile = Profile.objects.get(name__iexact=profile_name)
    #     pokedex = Pokedex.objects.get(profile=profile)
    #     page = self.paginate_queryset(
    #         pokedex.entries.all().order_by('pokemon__dex_number'))
    #     serialized = PokedexEntrySerializer(page, many=True)
    #     return self.get_paginated_response(serialized.data)

    # pylint: disable=no-self-use
    def create(self, request, profile_name=None):
        """
        Create a PokedexEntry

        :param request: Django Request
        :param profile_name: Name of the profile to create PokedexEntry for
        :return: Response code
        """
        if not request.user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        profile = Profile.objects.get(name__iexact=profile_name)
        if request.user.id != profile.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        form = CollectionForm(request.data)
        if form.is_valid():
            collection = Pokedex.objects.create(
                name=form.data.get('name')
            )
            collection.profile.add(profile)
            collection.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

# pylint: disable=too-many-ancestors
""" View Set for PokedexEntry Serializer """
from rest_framework import viewsets, status
from rest_framework.response import Response
from api.models.pokedex_entry import PokedexEntry
from api.models.pokemon import Pokemon
from api.models.image import Image
from api.models.profile import Profile
from api.models.pokedex import Pokedex
from api.serializers.pokedex_entry import PokedexEntrySerializer
from api.forms.pokedex_entry import PokedexEntryForm


class PokedexEntryViewSet(viewsets.GenericViewSet,
                          viewsets.mixins.ListModelMixin):
    """
    View Set for PokedexEntry Serializer
    """

    queryset = PokedexEntry.objects.all().order_by('pokemon__dex_number')
    serializer_class = PokedexEntrySerializer

    # pylint: disable=arguments-differ
    def list(self, request, profile_name=None):
        """
        List the entries from the supplied Profile's pokedex

        :param request: Django Request
        :param profile_name: Name of the profile to fetch PokedexEntries from
        :return: List of PokedexEntries
        """
        profile = Profile.objects.get(name__iexact=profile_name)
        pokedex = Pokedex.objects.get(profile=profile)
        page = self.paginate_queryset(
            pokedex.entries.all().order_by('pokemon__dex_number'))
        serialized = PokedexEntrySerializer(page, many=True)
        return self.get_paginated_response(serialized.data)

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
        form = PokedexEntryForm(request.data)
        if form.is_valid():
            pokemon = Pokemon.objects.get(id=form.data.get('pokemon'))
            image = Image.objects.get(id=form.data.get('image'))
            entry = PokedexEntry.objects.create(
                pokemon=pokemon,
                image=image
            )
            pokedex = Pokedex.objects.get(profile=profile)
            pokedex.entries.add(entry)
            pokedex.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

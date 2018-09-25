# pylint: disable=too-many-ancestors
""" View Set for Collection Serializer """
from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from api.models.profile import Profile
from api.models.collection import Collection
from api.serializers.collection import CollectionSerializer
from api.forms.collections import CollectionForm


class CollectionsViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.CreateModelMixin):
    """
    View Set for Collection Serializer
    """

    queryset = Collection.objects.all().order_by('id')
    serializer_class = CollectionSerializer

    # pylint: disable=no-self-use
    def create(self, request, profile_name=None):
        """
        Create a Collection

        :param request: Django Request
        :param profile_name: Name of the profile to create Collection for
        :return: Response code
        """
        if not request.user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        profile = Profile.objects.get(name__iexact=profile_name)
        if request.user.id != profile.user.id:
            return Response(status=status.HTTP_403_FORBIDDEN)
        form = CollectionForm(request.data)
        if form.is_valid():
            collection = Collection.objects.create(
                name=form.data.get('name')
            )
            collection.profile.add(profile)
            collection.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

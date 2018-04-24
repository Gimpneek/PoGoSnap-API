# pylint: disable=too-many-ancestors
""" View Set for Profile Serializer """
from rest_framework import viewsets
from api.models.profile import Profile
from api.serializers.profile import ProfileSerializer


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View Set for Profile Serializer
    """

    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

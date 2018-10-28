# pylint: disable=too-many-ancestors
""" View Set for Profile Serializer """
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from api.models.profile import Profile
from api.serializers.profile import ProfileSerializer


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View Set for Profile Serializer
    """

    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer
    lookup_field = 'name'

    def get_queryset(self):
        """ Override the queryset so it's case insensitive """
        name = self.kwargs.get('name')
        if name:
            return Profile.objects.filter(name__iexact=name)
        return Profile.objects.all().order_by('id')

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        user_id = request.user.id
        if not user_id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        profile = Profile.objects.get(user__id=user_id)
        return Response(data=ProfileSerializer(profile).data)

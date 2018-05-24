# pylint: disable=too-many-ancestors
""" View Set for Profile's Images Serializer """
from rest_framework import viewsets
from api.models.image import Image
from api.models.profile import Profile
from api.serializers.image import ImageSerializer


class ProfileImageViewSet(viewsets.GenericViewSet,
                          viewsets.mixins.ListModelMixin):
    """
    View Set for Profile's Images Serializer
    """

    queryset = Image.objects.all().order_by('id')
    serializer_class = ImageSerializer

    # pylint: disable=arguments-differ
    def list(self, request, profile_pk=None):
        """
        List the images from the supplied Profile

        :param request: Django Request
        :param profile_pk: ID of the profile to fetch Images from
        :return: List of Images
        """
        profile = Profile.objects.get(id=profile_pk)
        images = Image.objects.filter(profile=profile)
        page = self.paginate_queryset(
            images.all().order_by('id'))
        serialized = ImageSerializer(page, many=True)
        return self.get_paginated_response(serialized.data)

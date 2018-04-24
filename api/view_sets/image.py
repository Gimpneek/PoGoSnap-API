# pylint: disable=too-many-ancestors
""" View Set for Image Serializer """
from rest_framework import viewsets
from api.models.image import Image
from api.serializers.image import ImageSerializer


class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View Set for Image Serializer
    """

    queryset = Image.objects.all().order_by('id')
    serializer_class = ImageSerializer

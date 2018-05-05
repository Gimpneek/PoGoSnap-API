# pylint: disable=too-many-ancestors
""" View Set for Image Serializer """
from rest_framework import viewsets, status
from rest_framework.response import Response
from api.models.image import Image
from api.models.profile import Profile
from api.models.pokemon import Pokemon
from api.serializers.image import ImageSerializer
from api.forms.image import ImageForm


class ImageViewSet(viewsets.ModelViewSet):
    """
    View Set for Image Serializer
    """

    queryset = Image.objects.all().order_by('id')
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        """
        Create an Image

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if not request.user.id:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        form = ImageForm(request.data)
        if form.is_valid():
            profile = Profile.objects.get(user=request.user.id)
            pokemon = Pokemon.objects.get(id=form.data.get('pokemon'))
            Image.objects.create(
                url=form.cleaned_data.get('url'),
                pokemon=pokemon,
                profile=profile
            )
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

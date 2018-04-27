# -*- coding: utf-8 -*-
""" Form definition for Image """
from api.models.image import Image
from django.forms.models import ModelForm


class ImageForm(ModelForm):
    """ Image form"""

    class Meta(object):
        """ Metaclass for Image form """
        model = Image
        fields = (
            'url',
            'pokemon'
        )

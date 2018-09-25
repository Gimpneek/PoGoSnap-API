# -*- coding: utf-8 -*-
# pylint: disable=useless-object-inheritance
""" Form definition for Image """
from django.forms.models import ModelForm
from api.models.image import Image


class ImageForm(ModelForm):
    """ Image form"""

    class Meta(object):
        """ Metaclass for Image form """
        model = Image
        fields = (
            'image',
            'pokemon'
        )

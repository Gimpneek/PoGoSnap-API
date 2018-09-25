# -*- coding: utf-8 -*-
""" Form definition for Collection """
from django.forms.models import ModelForm
from api.models.pokedex import Pokedex


class CollectionForm(ModelForm):
    """ Collection form"""

    class Meta(object):
        """ Metaclass for Collection form """
        model = Pokedex
        fields = (
            'name',
        )

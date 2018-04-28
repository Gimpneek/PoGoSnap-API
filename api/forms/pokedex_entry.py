# -*- coding: utf-8 -*-
""" Form definition for PokedexEntry """
from django.forms.models import ModelForm
from api.models.pokedex_entry import PokedexEntry


class PokedexEntryForm(ModelForm):
    """ PokedexEntry form"""

    class Meta(object):
        """ Metaclass for PokedexEntry form """
        model = PokedexEntry
        fields = (
            'pokemon',
            'image'
        )

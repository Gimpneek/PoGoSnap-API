# -*- coding: utf-8 -*-
""" Form definition for CollectionEntry """
from django.forms.models import ModelForm
from api.models.collection_entry import CollectionEntry


class CollectionEntryForm(ModelForm):
    """ CollectionEntry form"""

    class Meta(object):
        """ Metaclass for CollectionEntry form """
        model = CollectionEntry
        fields = (
            'image'
        )

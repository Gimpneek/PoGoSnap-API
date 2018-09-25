# -*- coding: utf-8 -*-
""" Form definition for Collection """
from django.forms.models import ModelForm
from api.models.collection import Collection


class CollectionForm(ModelForm):
    """ Collection form"""

    class Meta(object):
        """ Metaclass for Collection form """
        model = Collection
        fields = (
            'name',
        )

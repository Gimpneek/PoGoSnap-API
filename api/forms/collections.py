# -*- coding: utf-8 -*-
# pylint: disable=useless-object-inheritance
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
            'type'
        )

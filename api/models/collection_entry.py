# -*- coding: utf-8 -*-
""" Model definition of Image """
from django.db import models
from api.models.image import Image


class CollectionEntry(models.Model):
    """
    Model for Collection entries
    """
    image = models.ForeignKey(Image, on_delete=models.DO_NOTHING)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ String representation of Collection Entry object """
        return "{0} image in {1}".format(
            self.image.pokemon.name, self.collection_set.first())

# -*- coding: utf-8 -*-
""" Model definition of Image """
from django.db import models
from api.models.image import Image


class PokedexEntry(models.Model):
    """
    Model for Pokedex entries
    """
    # pokemon = models.ForeignKey(Pokemon, on_delete=models.DO_NOTHING)
    image = models.ForeignKey(Image, on_delete=models.DO_NOTHING)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ String representation of Pokedex Entry object """
        return "{0} image in {1}".format(
            self.image.pokemon.name, self.pokedex_set.first())

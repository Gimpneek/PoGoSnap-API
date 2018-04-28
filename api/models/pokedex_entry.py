# -*- coding: utf-8 -*-
""" Model definition of Image """
from django.db import models
from api.models.pokemon import Pokemon
from api.models.image import Image


class PokedexEntry(models.Model):
    """
    Model for Pokedex entries
    """
    pokemon = models.ForeignKey(Pokemon, on_delete=models.DO_NOTHING)
    image = models.ForeignKey(Image, on_delete=models.DO_NOTHING)

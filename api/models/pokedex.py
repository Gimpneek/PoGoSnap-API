# -*- coding: utf-8 -*-
""" Model definition of Pokedex """
from django.db import models
from api.models.profile import Profile
from api.models.pokedex_entry import PokedexEntry


class Pokedex(models.Model):
    """ Pokedex model """

    entries = models.ManyToManyField(PokedexEntry, blank=True)
    profile = models.OneToOneField(Profile, on_delete=models.DO_NOTHING)

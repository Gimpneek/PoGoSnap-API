# -*- coding: utf-8 -*-
""" Model definition of Image """
from django.db import models
from api.models.pokemon import Pokemon
from api.models.profile import Profile


class Image(models.Model):
    """ Image model """

    url = models.URLField()
    pokemon = models.OneToOneField(Pokemon, on_delete=models.DO_NOTHING)
    profile = models.OneToOneField(Profile, on_delete=models.DO_NOTHING)

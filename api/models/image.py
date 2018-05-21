# -*- coding: utf-8 -*-
""" Model definition of Image """
from django.db import models
from api.models.pokemon import Pokemon
from api.models.profile import Profile


class Image(models.Model):
    """ Image model """

    url = models.URLField()
    pokemon = models.ForeignKey(Pokemon, on_delete=models.DO_NOTHING)
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)

    def __str__(self):
        """ String representation of Image """
        return "Picture of {0} by {1}".format(self.pokemon, self.profile)

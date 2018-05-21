# -*- coding: utf-8 -*-
""" Model definition of Pokemon """
from django.db import models


class Pokemon(models.Model):
    """ Pokemon Model Definition """
    name = models.CharField(
        help_text='Name of the Pokemon',
        max_length=128
    )
    dex_number = models.SmallIntegerField(
        help_text='Number of the Pokemon in the Pokedex'
    )

    def __str__(self):
        """ String represenation of Pokemon """
        return "{0}(#{1})".format(self.name, self.dex_number)

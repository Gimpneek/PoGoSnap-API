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

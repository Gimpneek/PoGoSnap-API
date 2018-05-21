# -*- coding: utf-8 -*-
""" Model definition of User Profile """
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """ User Profile """
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    name = models.CharField(
        help_text='Name of the user',
        max_length=128
    )
    location = models.CharField(
        help_text='Location of the user',
        max_length=128
    )
    silph_card = models.CharField(
        help_text='URL of User\'s Silph Card',
        max_length=128
    )

    def __str__(self):
        """ String representation of object """
        return "{0}".format(self.user.username)

# -*- coding: utf-8 -*-
# pylint: disable=no-self-use,no-self-argument
""" Model definition of Pokedex """
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models.profile import Profile
from api.models.pokedex_entry import PokedexEntry


class Pokedex(models.Model):
    """ Pokedex model """

    entries = models.ManyToManyField(PokedexEntry, blank=True)
    profile = models.ManyToManyField(Profile)
    name = models.CharField(max_length=256, default='Pokedex')

    def __str__(self):
        """ String representation of the Pokedex object """
        return "{0}'s Pokedex".format(self.profile.all()[0])

    @receiver(post_save, sender=Profile)
    def create_profile_pokedex(sender, instance, created, **kwargs):
        """
        Create a Pokedex whenever a Profile has been created

        :param instance: created instance of Profile
        :param created: if Profile was created
        :param kwargs: keyword args
        """
        if created:
            pokedex = Pokedex.objects.create(name='Pokedex')
            pokedex.profile.add(instance)
            pokedex.save()

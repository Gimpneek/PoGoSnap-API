# -*- coding: utf-8 -*-
# pylint: disable=no-self-use,no-self-argument
""" Model definition of Collection """
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models.profile import Profile
from api.models.collection_entry import CollectionEntry


class Collection(models.Model):
    """ Collection model """

    entries = models.ManyToManyField(CollectionEntry, blank=True)
    profile = models.ManyToManyField(Profile)
    name = models.CharField(max_length=256, default='Pokedex')

    def __str__(self):
        """ String representation of the Collection object """
        return "{0}'s {1}".format(self.profile.all()[0], self.name)

    @receiver(post_save, sender=Profile)
    def create_profile_pokedex(sender, instance, created, **kwargs):
        """
        Create a Pokedex whenever a Profile has been created

        :param instance: created instance of Profile
        :param created: if Profile was created
        :param kwargs: keyword args
        """
        if created:
            pokedex = Collection.objects.create(name='Pokedex')
            pokedex.profile.add(instance)
            pokedex.save()

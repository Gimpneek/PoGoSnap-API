# -*- coding: utf-8 -*-
# pylint: disable=no-self-use,no-self-argument
""" Model definition of User Profile """
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver


class Profile(models.Model):
    """ User Profile """
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    name = models.CharField(
        help_text='Name of the user',
        max_length=128,
        unique=True
    )
    location = models.CharField(
        help_text='Location of the user',
        max_length=128
    )
    silph_card = models.CharField(
        help_text='URL of User\'s Silph Card',
        max_length=128
    )

    featured_image = models.ForeignKey(
        'api.Image',
        related_name='featured_image',
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ String representation of object """
        return "{0}".format(self.user.username)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        """
        Create Profile when User object is created

        :param instance: Instance of the User Object
        :param created: if the object was created
        :param kwargs: keyword arguments
        """
        if created:
            Profile.objects.create(
                user=instance,
                name=instance.username,
                location='',
                silph_card=''
            )

# -*- coding: utf-8 -*-
""" Model definition of Image """
import uuid
import os
from django.db import models
from api.models.pokemon import Pokemon
from api.models.profile import Profile


def get_file_path(instance, filename):
    """
    Create a UUID based filename for the file being uploaded

    :param instance: Instance of model
    :param filename: Name of the file
    :return: path to save file too
    """
    ext = filename.split('.')[-1]
    filename = "{0}.{1}".format(uuid.uuid4(), ext)
    return os.path.join('usercontent', filename)


class Image(models.Model):
    """ Image model """

    image = models.FileField(
        upload_to=get_file_path,
        default=None)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.DO_NOTHING)
    profile = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)

    def __str__(self):
        """ String representation of Image """
        return "Picture of {0} by {1}".format(self.pokemon, self.profile)

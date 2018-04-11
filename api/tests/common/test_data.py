""" Common Test Data and functions """
from django.contrib.auth.models import User
from api.models.profile import Profile
from api.models.pokemon import Pokemon


POKEMON_NAME = 'Mew'
POKEMON_NUMBER = 150

USER_NAME = 'test'

PROFILE_NAME = 'test'
PROFILE_LOCATION = 'Leeds, UK'
PROFILE_SILPH_CARD_URL = 'https://sil.ph/test'

IMAGE_URL = 'https://test.com/meh.jpg'


def create_user():
    """
    Create a user

    :return: User object
    """
    return User.objects.create(username=USER_NAME)


def create_profile():
    """
    Create a Profile

    :return: Profile object
    """
    return Profile.objects.create(
        user=create_user(),
        name=PROFILE_NAME,
        location=PROFILE_LOCATION,
        silph_card=PROFILE_SILPH_CARD_URL
    )


def create_pokemon():
    """
    Create a Pokemon

    :return: Pokemon object
    """
    return Pokemon.objects.create(
        name=POKEMON_NAME,
        dex_number=POKEMON_NUMBER
    )

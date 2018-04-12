""" Common Test Data and functions """
from django.contrib.auth.models import User
from api.models.profile import Profile
from api.models.pokemon import Pokemon
from api.models.image import Image
from api.models.pokedex_entry import PokedexEntry


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
    User.objects.get_or_create(username=USER_NAME)
    return User.objects.get(username=USER_NAME)


def create_profile():
    """
    Create a Profile

    :return: Profile object
    """
    Profile.objects.get_or_create(
        user=create_user(),
        name=PROFILE_NAME,
        location=PROFILE_LOCATION,
        silph_card=PROFILE_SILPH_CARD_URL
    )
    return Profile.objects.get(name=PROFILE_NAME)


def create_pokemon():
    """
    Create a Pokemon

    :return: Pokemon object
    """
    return Pokemon.objects.create(
        name=POKEMON_NAME,
        dex_number=POKEMON_NUMBER
    )


def create_image():
    """
    Create an image

    :return: Image object
    """
    return Image.objects.create(
        url=IMAGE_URL,
        pokemon=create_pokemon(),
        profile=create_profile()
    )


def create_pokedex_entry():
    """
    Create a pokedex entry

    :return: PokedexEntry object
    """
    return PokedexEntry.objects.create(
        image=create_image(),
        pokemon=create_pokemon()
    )

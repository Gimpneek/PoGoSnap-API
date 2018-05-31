""" Common Test Data and functions """
from django.contrib.auth.models import User
from django.core.files import File
from unittest.mock import MagicMock
from api.models.profile import Profile
from api.models.pokemon import Pokemon
from api.models.image import Image
from api.models.pokedex_entry import PokedexEntry
from api.models.pokedex import Pokedex


POKEMON_NAME = 'Mew'
POKEMON_NUMBER = 150

USER_NAME = 'test'
ANOTHER_USER = 'test2'

PROFILE_NAME = 'test'
PROFILE_LOCATION = 'Leeds, UK'
PROFILE_SILPH_CARD_URL = 'https://sil.ph/test'

ANOTHER_PROFILE_NAME = 'test2'
ANOTHER_PROFILE_LOCATION = 'London, UK'
ANOTHER_PROFILE_SILPH_CARD_URL = 'https://sil.ph/test2'

IMAGE_URL = 'https://test.com/meh.jpg'
IMAGE_DESC = 'Image of a pokemon'


def create_user():
    """
    Create a user

    :return: User object
    """
    user = User.objects.get_or_create(username=USER_NAME)[0]
    user.set_password(USER_NAME)
    user.save()
    return User.objects.get(username=USER_NAME)


def create_another_user():
    """
    Create another user
    """
    user = User.objects.get_or_create(username=ANOTHER_USER)[0]
    user.set_password(ANOTHER_USER)
    user.save()
    return User.objects.get(username=ANOTHER_USER)


def create_profile():
    """
    Create a Profile

    :return: Profile object
    """
    create_user()
    profile = Profile.objects.get(name=USER_NAME)
    profile.name = PROFILE_NAME
    profile.location = PROFILE_LOCATION
    profile.silph_card = PROFILE_SILPH_CARD_URL
    profile.save()
    return profile


def create_another_profile():
    """
    Create another profile
    """
    create_another_user()
    profile = Profile.objects.get(name=ANOTHER_USER)
    profile.name = ANOTHER_PROFILE_NAME
    profile.location = ANOTHER_PROFILE_LOCATION
    profile.silph_card = ANOTHER_PROFILE_SILPH_CARD_URL
    profile.save()
    return profile


def create_pokemon():
    """
    Create a Pokemon

    :return: Pokemon object
    """
    return Pokemon.objects.create(
        name=POKEMON_NAME,
        dex_number=POKEMON_NUMBER
    )


def create_image(profile=None, pokemon=None):
    """
    Create an image

    :param profile: Profile object
    :param pokemon: Pokemon object
    :return: Image object
    """
    file_mock = MagicMock(spec=File, name='FileMock')
    file_mock.name = 'test.jpg'
    if not profile:
        profile = create_profile()
    if not pokemon:
        pokemon = create_pokemon()
    return Image.objects.create(
        image=file_mock,
        pokemon=pokemon,
        profile=profile,
        description=IMAGE_DESC
    )


def create_pokedex_entry(image=None, pokemon=None):
    """
    Create a pokedex entry

    :param image: Image object
    :param pokemon: Pokemon object
    :return: PokedexEntry object
    """
    if not image:
        image = create_image()
    if not pokemon:
        pokemon = create_pokemon()
    return PokedexEntry.objects.create(
        image=image,
        pokemon=pokemon
    )


def create_pokedex(profile=None, entries=None):
    """
    Create a pokedex object

    :param profile: Profile object
    :param entries: A list of PokedexEntry objects
    :return: Pokedex object
    """
    if not profile:
        profile = create_profile()
    if not entries:
        entries = [create_pokedex_entry()]
    pokedex = Pokedex.objects.get_or_create(
        profile=profile
    )[0]
    for entry in entries:
        pokedex.entries.add(entry)
    pokedex.save()
    return pokedex

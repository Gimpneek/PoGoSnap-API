""" Common Test Data and functions """
from django.contrib.auth.models import User
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
    Profile.objects.get_or_create(
        user=create_user(),
        name=PROFILE_NAME,
        location=PROFILE_LOCATION,
        silph_card=PROFILE_SILPH_CARD_URL
    )
    return Profile.objects.get(name=PROFILE_NAME)


def create_another_profile():
    """
    Create another profile
    """
    Profile.objects.get_or_create(
        user=create_another_user(),
        name=ANOTHER_PROFILE_NAME,
        location=ANOTHER_PROFILE_LOCATION,
        silph_card=ANOTHER_PROFILE_SILPH_CARD_URL
    )
    return Profile.objects.get(name=ANOTHER_PROFILE_NAME)


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
    if not profile:
        profile = create_profile()
    if not pokemon:
        pokemon = create_pokemon()
    return Image.objects.create(
        pokemon=pokemon,
        profile=profile
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
    pokedex = Pokedex.objects.create(
        profile=profile,
    )
    for entry in entries:
        pokedex.entries.add(entry)
    pokedex.save()
    return pokedex

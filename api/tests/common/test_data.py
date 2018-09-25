""" Common Test Data and functions """
from django.contrib.auth.models import User
from django.core.files import File
from unittest.mock import MagicMock
from uuid import uuid4
from datetime import datetime, timedelta
from oauth2_provider.models import Application, AccessToken
from api.models.profile import Profile
from api.models.pokemon import Pokemon
from api.models.image import Image
from api.models.pokedex_entry import PokedexEntry
from api.models.collection import Collection
import pytz


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


def create_pokedex_entry(image=None):
    """
    Create a pokedex entry

    :param image: Image object
    :return: PokedexEntry object
    """
    if not image:
        image = create_image()
    return PokedexEntry.objects.create(
        image=image
    )


def create_collection(profile=None, entries=None):
    """
    Create a collection object

    :param profile: Profile object
    :param entries: A list of PokedexEntry objects
    :return: Collection object
    """
    if not profile:
        create_profile()
    if not entries:
        entries = [create_pokedex_entry()]
    pokedex = Collection.objects.get(name='Pokedex', profile=profile)
    for entry in entries:
        pokedex.entries.add(entry)
    pokedex.save()
    return pokedex


def create_facebook_app(user=None):
    """
    Create Facebook Application for Django oAuth2

    :param user: User object
    :return: Application object
    """
    if not user:
        user = create_user()
    facebook = Application.objects.create(
        client_id=str(uuid4()),
        client_type='confidential',
        authorization_grant_type='password',
        client_secret='test_facebook_secret',
        name='Test Facebook',
        user=user
    )
    return facebook


def create_access_token(user=None, app=None):
    """
    Create access token for supplied user using supplied oAuth2 app

    :param user: User object
    :param app: Application object
    :return: Access Token
    """
    if not user:
        user = create_user()
    if not app:
        app = create_facebook_app(user)
    now = datetime.now(tz=pytz.UTC)
    expiry_datetime = now + timedelta(days=1)
    token = AccessToken.objects.create(
        user=user,
        application=app,
        token=str(uuid4()),
        expires=expiry_datetime
    )
    return token

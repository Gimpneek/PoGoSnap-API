""" Admin setup """
from django.contrib import admin
from api.models.profile import Profile
from api.models.pokemon import Pokemon
from api.models.image import Image
from api.models.pokedex_entry import PokedexEntry
from api.models.pokedex import Pokedex

# Register your models here.
admin.site.register(Profile)
admin.site.register(Pokemon)
admin.site.register(Image)
admin.site.register(PokedexEntry)
admin.site.register(Pokedex)

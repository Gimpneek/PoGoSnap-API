from django.contrib import admin
from api.models.profile import Profile
from api.models.pokemon import Pokemon
from api.models.image import Image
from api.models.pokedex_entry import PokedexEntry
from api.models.pokedex import Pokedex

# Register your models here.
admin.register(Profile)
admin.register(Pokemon)
admin.register(Image)
admin.register(PokedexEntry)
admin.register(Pokedex)

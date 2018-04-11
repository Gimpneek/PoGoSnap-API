from django.contrib import admin
from api.models.profile import Profile
from api.models.pokemon import Pokemon
from api.models.image import Image

# Register your models here.
admin.register(Profile)
admin.register(Pokemon)
admin.register(Image)

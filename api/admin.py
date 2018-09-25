""" Admin setup """
from django.contrib import admin
from api.models.profile import Profile
from api.models.pokemon import Pokemon
from api.models.image import Image
from api.models.collection_entry import CollectionEntry
from api.models.collection import Collection

# Register your models here.
admin.site.register(Profile)
admin.site.register(Pokemon)
admin.site.register(Image)
admin.site.register(CollectionEntry)
admin.site.register(Collection)

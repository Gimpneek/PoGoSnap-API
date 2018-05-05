""" URLS for api module """
from django.conf.urls import url, include
from rest_framework_nested import routers
from rest_framework_jwt.views import obtain_jwt_token
from api.view_sets.profile import ProfileViewSet
from api.view_sets.image import ImageViewSet
from api.view_sets.pokedex_entry import PokedexEntryViewSet

API_ROUTER = routers.SimpleRouter()
API_ROUTER.register(r'profiles', ProfileViewSet, base_name='profiles')
API_ROUTER.register(r'images', ImageViewSet, base_name='images')

PROFILE_ROUTER = routers.NestedSimpleRouter(
    API_ROUTER,
    r'profiles',
    lookup='profile'
)
PROFILE_ROUTER.register(r'pokedex', PokedexEntryViewSet, base_name='pokedex')


urlpatterns = [
    url('v1/', include(API_ROUTER.urls)),
    url('v1/', include(PROFILE_ROUTER.urls)),
    url('v1/api-token-auth/', obtain_jwt_token)
]

API_URLS = urlpatterns, 'api', 'api'

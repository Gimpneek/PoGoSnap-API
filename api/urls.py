""" URLS for api module """
from django.conf.urls import url, include
from rest_framework_nested import routers
from api.view_sets.profile import ProfileViewSet
from api.view_sets.image import ImageViewSet
from api.view_sets.collections import CollectionsViewSet
from api.view_sets.collection_entries import CollectionEntriesViewSet
from api.view_sets.profiles_images import ProfileImageViewSet

API_ROUTER = routers.SimpleRouter()
API_ROUTER.register(r'profiles', ProfileViewSet, base_name='profiles')
API_ROUTER.register(r'images', ImageViewSet, base_name='images')

PROFILE_ROUTER = routers.NestedSimpleRouter(
    API_ROUTER,
    r'profiles',
    lookup='profile'
)
PROFILE_ROUTER.register(
    r'collections',
    CollectionsViewSet,
    base_name='collections'
)
PROFILE_ROUTER.register(
    r'images',
    ProfileImageViewSet,
    base_name='profile_images'
)

COLLECTIONS_ROUTER = routers.NestedSimpleRouter(
    PROFILE_ROUTER,
    r'collections',
    lookup='collections'
)

COLLECTIONS_ROUTER.register(
    r'entries',
    CollectionEntriesViewSet,
    base_name='entries'
)

urlpatterns = [
    url('v1/', include(API_ROUTER.urls)),
    url('v1/', include(PROFILE_ROUTER.urls)),
    url('v1/', include(COLLECTIONS_ROUTER.urls))
]

API_URLS = urlpatterns, 'api', 'api'

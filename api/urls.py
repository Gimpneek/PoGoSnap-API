""" URLS for api module """
from django.conf.urls import url, include
from rest_framework import routers
from api.view_sets.profile import ProfileViewSet

API_ROUTER = routers.SimpleRouter()
API_ROUTER.register(r'profiles', ProfileViewSet)

urlpatterns = [
    url('v1/', include(API_ROUTER.urls))
]

API_URLS = urlpatterns, 'api', 'api'

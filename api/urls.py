""" URLS for api module """
from django.conf.urls import url, include
from rest_framework import routers
from api.view_sets.profile import ProfileViewSet

api_router = routers.SimpleRouter()
api_router.register(r'users', ProfileViewSet)

urlpatterns = [
    url(r'v1', include(api_router.urls))
]

api_urls = urlpatterns, 'api', 'api'

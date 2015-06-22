"""
birdo URL Configuration
"""

from django.conf.urls import include, url
from django.contrib import admin

from birds.views import BirdInterface


urlpatterns = [
    url(r'^api/', include('api.urls', namespace='api')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*$', BirdInterface.as_view(), name='birds'),
]

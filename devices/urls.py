from __future__ import unicode_literals

from django.conf.urls import url

from .views import (
    DeviceListCreateAPIView,
)
from . import views

urlpatterns = [
    # url(r'^$', DeviceListCreateAPIView.as_view(), name="list"),
    url(r'^$', views.index, name='index'),
    url(r'^secure$', views.secure, name='secure'),
]

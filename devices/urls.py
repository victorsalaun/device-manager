from __future__ import unicode_literals

from django.conf.urls import url

from .views import (
    DeviceListCreateAPIView,
)

urlpatterns = [
    url(r'^$', DeviceListCreateAPIView.as_view(), name="list"),
]

from __future__ import unicode_literals

from django.conf.urls import url

from .api_views import (
    APIDeviceListView
)

from .views import (
    DeviceListView
)

urlpatterns = [
    url(r'^list/$', DeviceListView.as_view(), name='device_list'),
]

api_urls = [
    url(r'^devices/$', APIDeviceListView.as_view(), name='device-list'),
]

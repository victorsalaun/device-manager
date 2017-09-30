from __future__ import absolute_import, unicode_literals

from rest_framework import generics

from .models import Device
from .serializers import DeviceSerializer


class APIDeviceListView(generics.ListCreateAPIView):
    queryset = Device.objects.all()

    def get_serializer_class(self):
        return DeviceSerializer

    def get(self, *args, **kwargs):
        """
        Returns a list of all the cabinets.
        """
        return super(APIDeviceListView, self).get(*args, **kwargs)

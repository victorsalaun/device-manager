from __future__ import absolute_import, unicode_literals

from rest_framework.generics import ListCreateAPIView

from devices.models import Device
from devices.serializers import DeviceSerializer


class DeviceListCreateAPIView(ListCreateAPIView):
    serializer_class = DeviceSerializer

    def get_queryset(self):
        return Device.objects.all()

    def perform_create(self, serializer):
        serializer.save()

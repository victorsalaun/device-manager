from __future__ import absolute_import, unicode_literals

from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from devices.models import Device


class DeviceListView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'devices/device_list.html'

    def get(self, request):
        queryset = Device.objects.all()
        return Response({'devices': queryset})

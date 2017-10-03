from __future__ import absolute_import, unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from rest_framework.generics import ListAPIView

from devices.models import Device
from devices.serializers import DeviceSerializer


class DeviceListCreateAPIView(ListAPIView):
    serializer_class = DeviceSerializer

    @login_required
    def get_queryset(self, request):
        return Device.objects.all()

    @login_required
    def perform_create(self, request, serializer):
        serializer.save()


def index(request):
    return HttpResponse('You\'re at the index. <a href="/secure">Secure</a>')


@login_required
def secure(request):
    return HttpResponse('Secure page. <a href="/openid/logout">Logout</a>')

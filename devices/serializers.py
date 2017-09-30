from rest_framework import serializers

from .models import Device


class DeviceSerializer(serializers.ModelSerializer):
    os = serializers.CharField(read_only=True)
    os_version = serializers.CharField(required=False)
    brand = serializers.SlugField(required=False)
    name = serializers.SlugField(required=False)

    class Meta:
        model = Device
        fields = (
            'os',
            'os_version',
            'brand',
            'name',
        )

    def create(self, validated_data):
        os = self.context.get('os', None)
        os_version = self.context.get('os_version', None)
        brand = self.context.get('brand', None)
        name = self.context.get('name', None)

        device = Device.objects.create(os=os, os_version=os_version, brand=brand, name=name, **validated_data)

        return device

    def get_os(self, instance):
        return instance.os

    def get_os_version(self, instance):
        return instance.os_version

    def get_brand(self, instance):
        return instance.brand

    def get_name(self, instance):
        return instance.name

from django.db import models
from django.utils.encoding import smart_text as smart_unicode


class Device(models.Model):
    os = models.CharField(max_length=128, blank=True)
    os_version = models.CharField(max_length=128, blank=True)
    brand = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=128, blank=True)

    class Meta:
        verbose_name = "Device"
        verbose_name_plural = "Devices"

    def __str__(self):
        return self.name

    def __unicode__(self):
        return smart_unicode(self.name)

from django.db import models


class Device(models.Model):
    os = models.CharField(max_length=128, blank=True)
    os_version = models.CharField(max_length=128, blank=True)
    brand = models.CharField(max_length=128, blank=True)
    name = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.name

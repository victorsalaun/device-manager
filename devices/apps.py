from django.apps import apps, AppConfig


class DevicesApp(AppConfig):
    name = 'devices'
    has_tests = False

    def ready(self):
        super(DevicesApp, self).ready()
        Device = apps.get_model(
            app_label='devices', model_name='Device'
        )

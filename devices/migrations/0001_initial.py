from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                (
                    'id', models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, max_length=200, verbose_name='ID'
                    )
                ),
                (
                    'os', models.CharField(
                        db_index=True, max_length=200, verbose_name='OS'
                    )
                ),
                (
                    'os_version', models.CharField(
                        max_length=200, verbose_name='OS Version'
                    )
                ),
                (
                    'brand', models.CharField(
                        max_length=200, verbose_name='Brand'
                    )
                ),
                (
                    'name', models.CharField(
                        max_length=200, verbose_name='Name'
                    )
                ),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
            },
        ),
    ]

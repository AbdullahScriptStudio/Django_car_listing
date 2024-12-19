# Generated by Django 5.1.4 on 2024-12-06 12:54

import localflavor.pk.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_location_alter_profile_location_delete_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='post_code',
            field=localflavor.pk.models.PKPostCodeField(default='1111', max_length=5),
        ),
        migrations.AddField(
            model_name='location',
            name='state',
            field=localflavor.pk.models.PKPostCodeField(default='Punjab', max_length=5),
        ),
    ]

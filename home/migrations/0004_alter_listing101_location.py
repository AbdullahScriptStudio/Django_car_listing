# Generated by Django 5.1.4 on 2024-12-15 07:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_listing101_location'),
        ('users', '0006_alter_location_state_alter_profile_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing101',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location'),
        ),
    ]

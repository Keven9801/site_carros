# Generated by Django 5.1.2 on 2024-10-23 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_car_bo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='bo',
            new_name='bio',
        ),
    ]

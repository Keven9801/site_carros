# Generated by Django 5.1.2 on 2024-10-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=200)),
                ('factory_year', models.IntegerField(blank=True, null=True)),
                ('model_year', models.IntegerField(blank=True, null=True)),
                ('value', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]

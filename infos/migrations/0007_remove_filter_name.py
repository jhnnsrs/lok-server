# Generated by Django 3.2.19 on 2023-05-06 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0006_auto_20230506_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filter',
            name='name',
        ),
    ]

# Generated by Django 3.2.9 on 2021-12-22 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maktab_18', '0030_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='image',
        ),
    ]

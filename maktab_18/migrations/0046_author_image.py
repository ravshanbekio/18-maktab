# Generated by Django 3.2.9 on 2022-05-17 02:52

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maktab_18', '0045_thebestpupils'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=cloudinary.models.CloudinaryField(default='img/pngwing.com.png', max_length=255),
            preserve_default=False,
        ),
    ]

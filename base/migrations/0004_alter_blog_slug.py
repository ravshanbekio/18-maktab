# Generated by Django 3.2.9 on 2022-08-01 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

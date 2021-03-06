# Generated by Django 3.2.9 on 2022-04-21 17:53

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maktab_18', '0044_alter_examquestion_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheBestPupils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pupil_name', models.CharField(max_length=150)),
                ('about_pupil', models.TextField(max_length=700)),
                ('pupil_photo', cloudinary.models.CloudinaryField(max_length=255)),
                ('start_study_years', models.DateField()),
                ('end_study_years', models.DateField()),
                ('views', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': "Eng yaxshi o'quvchilar",
            },
        ),
    ]

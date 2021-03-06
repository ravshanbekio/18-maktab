# Generated by Django 3.2.9 on 2021-12-14 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maktab_18', '0009_delete_lesson'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='Fan')),
                ('cost', models.CharField(max_length=50, verbose_name='Narx')),
                ('teacher_name', models.CharField(max_length=200, verbose_name="O'qituvchi ismi")),
                ('in_week', models.IntegerField(verbose_name='Haftada')),
                ('time', models.CharField(max_length=13, verbose_name="Vaqt oralig'")),
                ('description', models.CharField(max_length=90, verbose_name='Tasvir')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, related_name='profiles', to=settings.AUTH_USER_MODEL, serialize=False, verbose_name='Користувач')),
                ('sex', models.CharField(max_length=20, verbose_name='Стать', choices=[('Man', 'Чоловік'), ('Woman', 'Жінка')])),
                ('avatar', models.ImageField(upload_to='upload/profile_images/', blank=True, verbose_name='Аватарка', help_text='Фото користувача')),
                ('profile_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення профіля')),
                ('profile_update', models.DateTimeField(auto_now=True, verbose_name='Дата оновлення профіля')),
            ],
            options={
                'verbose_name_plural': 'Профілі користувачів',
                'verbose_name': 'Профіль користувача',
                'db_table': 'profile',
            },
        ),
    ]

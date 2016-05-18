# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 20:20
from __future__ import unicode_literals

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_article_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, help_text='Зображення до статті', upload_to=blog.models.upload_location, verbose_name='Картинки'),
        ),
    ]

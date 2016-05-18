# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('navigation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('article_title', models.CharField(max_length=50, verbose_name='Назва статті')),
                ('article_text', models.TextField(verbose_name='Текст статті')),
                ('article_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('article_update', models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')),
                ('article_likes', models.IntegerField(default=0, verbose_name='Подобається')),
                ('article_image', models.ImageField(upload_to='upload/article_images/', blank=True, verbose_name='Картинки', help_text='Зображення до статті')),
                ('article_slug', models.SlugField(unique=True, verbose_name='Ім`я статті транслітом', blank=True)),
                ('article_category', models.ForeignKey(related_name='articles', to='navigation.Category', verbose_name='Категорія')),
            ],
            options={
                'verbose_name_plural': 'Статті',
                'verbose_name': 'Стаття',
                'db_table': 'articles',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('tag_title', models.CharField(max_length=50, verbose_name='Назва тега')),
                ('tag_name', models.SlugField(verbose_name='Ім`я тега транслітом')),
            ],
            options={
                'verbose_name_plural': 'Тегі',
                'verbose_name': 'Тег',
                'db_table': 'tags',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='article_tag',
            field=models.ManyToManyField(related_name='articles', to='blog.Tag', verbose_name='Тегі'),
        ),
    ]

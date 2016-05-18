# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('comments_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('comments_text', models.TextField(max_length=200, verbose_name='Текст коментаря')),
                ('comments_article', models.ForeignKey(related_name='comments', to='blog.Article', verbose_name='Коментар для статті')),
            ],
            options={
                'verbose_name_plural': 'Коментарі',
                'verbose_name': 'Коментар',
                'db_table': 'comments',
            },
        ),
    ]

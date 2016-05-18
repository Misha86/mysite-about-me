# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('loginsys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_user',
            field=models.ForeignKey(related_name='articles', to='loginsys.Profile', verbose_name='Автор статті'),
        ),
    ]

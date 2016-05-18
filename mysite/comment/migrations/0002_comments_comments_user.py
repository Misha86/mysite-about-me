# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
        ('loginsys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comments_user',
            field=models.ForeignKey(related_name='comments', to='loginsys.Profile', verbose_name='Автор коментаря'),
        ),
    ]

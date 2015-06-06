# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bird',
            options={'ordering': ('order', 'created')},
        ),
        migrations.AddField(
            model_name='bird',
            name='order',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bird',
            name='name',
            field=models.CharField(unique=True, max_length=255, db_index=True),
        ),
    ]

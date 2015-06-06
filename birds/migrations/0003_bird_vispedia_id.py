# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0002_auto_20150606_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='bird',
            name='vispedia_id',
            field=models.CharField(db_index=True, max_length=50, unique=True, null=True, blank=True),
        ),
    ]

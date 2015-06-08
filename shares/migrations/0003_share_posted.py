# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0002_auto_20150607_2224'),
    ]

    operations = [
        migrations.AddField(
            model_name='share',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 7, 22, 31, 18, 845927, tzinfo=utc)),
            preserve_default=False,
        ),
    ]

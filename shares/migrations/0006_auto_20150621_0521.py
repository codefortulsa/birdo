# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0005_auto_20150608_0539'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='birdsearchresult',
            options={'ordering': ('-created',), 'get_latest_by': 'created'},
        ),
    ]

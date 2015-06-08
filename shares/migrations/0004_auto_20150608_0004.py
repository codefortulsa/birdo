# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0003_share_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='network_id',
            field=models.BigIntegerField(help_text=b'ID specific to that network, prevents duplicate statuses'),
        ),
        migrations.AlterField(
            model_name='share',
            name='rel_lastrun',
            field=models.DateTimeField(null=True, verbose_name=b'Relevance last run', blank=True),
        ),
    ]

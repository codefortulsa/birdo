# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='share',
            options={},
        ),
        migrations.AddField(
            model_name='share',
            name='network_id',
            field=models.PositiveIntegerField(default=0, help_text=b'ID specific to that network, prevents duplicate statuses'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='share',
            unique_together=set([('network_id', 'network')]),
        ),
    ]

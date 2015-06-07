# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='share',
            name='network',
            field=models.SmallIntegerField(help_text=b'the network the share occurred', verbose_name=b'Social Network', choices=[(0, b'Unknown'), (1, b'Twitter'), (2, b'Facebook'), (3, b'Instagram')]),
        ),
    ]

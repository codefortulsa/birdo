# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0002_auto_20150621_0521'),
    ]

    operations = [
        migrations.AddField(
            model_name='birdpermutation',
            name='details',
            field=django_pgjson.fields.JsonField(null=True, blank=True),
        ),
    ]

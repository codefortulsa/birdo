# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permutationtype',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='bird',
            name='details',
            field=django_pgjson.fields.JsonField(null=True, blank=True),
        ),
    ]

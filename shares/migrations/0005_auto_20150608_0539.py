# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('birds', '0001_initial'),
        ('shares', '0004_auto_20150608_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='BirdSearchResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('last_network_id', models.BigIntegerField()),
                ('count', models.PositiveIntegerField()),
                ('target_bird', models.ForeignKey(to='birds.Bird')),
            ],
            options={
                'get_latest_by': 'created',
            },
        ),
        migrations.AlterModelOptions(
            name='share',
            options={'ordering': ('-posted',)},
        ),
        migrations.AlterField(
            model_name='searchtag',
            name='lastrun',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]

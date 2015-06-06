# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('user', models.CharField(help_text=b'the username of the sharer', max_length=50, verbose_name=b'User')),
                ('network', models.SmallIntegerField(help_text=b'the network the share occurred', verbose_name=b'Social Network', choices=[(0, b'Twitter'), (1, b'Facebook'), (2, b'Instagram')])),
                ('text', models.TextField()),
                ('rel', models.FloatField(default=0.0, help_text=b'how relevant the share is to birds', verbose_name=b'Relevance')),
                ('rel_lastrun', models.DateTimeField(verbose_name=b'Relevance last run')),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Tag Name')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='SearchTag',
            fields=[
                ('tag_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='shares.Tag')),
                ('enabled', models.BooleanField(default=True)),
                ('lastrun', models.DateTimeField()),
            ],
            options={
                'ordering': ('-modified', '-created'),
                'abstract': False,
                'get_latest_by': 'modified',
            },
            bases=('shares.tag',),
        ),
        migrations.AddField(
            model_name='share',
            name='tags',
            field=models.ManyToManyField(related_name='shares', to='shares.Tag'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import mptt.fields
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SharedBird',
            fields=[
                ('bird_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='birds.Bird')),
                ('shares', models.ManyToManyField(related_name='birds', to='shares.Share')),
            ],
            options={
                'abstract': False,
            },
            bases=('birds.bird',),
        ),
        migrations.AddField(
            model_name='bird',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', blank=True, to='birds.Bird', null=True),
        ),
    ]

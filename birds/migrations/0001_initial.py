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
                ('name', models.CharField(unique=True, max_length=255, db_index=True)),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('vispedia_id', models.CharField(db_index=True, max_length=50, unique=True, null=True, blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='birds.Bird', null=True)),
                ('shares', models.ManyToManyField(related_name='birds', to='shares.Share', blank=True)),
            ],
            options={
                'ordering': ('order', 'created'),
            },
        ),
        migrations.CreateModel(
            name='BirdPermutation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('vispedia_id', models.CharField(db_index=True, max_length=50, unique=True, null=True, blank=True)),
                ('bird', models.ForeignKey(related_name='permutations', to='birds.Bird')),
            ],
        ),
        migrations.CreateModel(
            name='PermutationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='birdpermutation',
            name='types',
            field=models.ManyToManyField(related_name='bird_perms', to='birds.PermutationType'),
        ),
    ]

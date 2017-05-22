# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('twitter_id', models.BigIntegerField()),
                ('username', models.CharField(max_length=25)),
                ('user', models.CharField(max_length=25)),
                ('language', models.CharField(max_length=4)),
                ('retweets', models.IntegerField()),
                ('favorites', models.IntegerField()),
                ('coordinates', models.CharField(max_length=50)),
                ('text', models.CharField(max_length=160)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('category', models.SmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=15)),
                ('valid', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=50)),
                ('admin', models.BinaryField()),
            ],
        ),
        migrations.CreateModel(
            name='UserRelations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('group', models.CharField(max_length=15)),
                ('user', models.ForeignKey(to='notwicias.User')),
            ],
        ),
    ]

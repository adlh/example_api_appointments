# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptedOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ScheduleOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('appointment', models.ForeignKey(related_name='options', to='api.Appointment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='appointment',
            name='owner',
            field=models.ForeignKey(related_name='appointments', to='api.Participant'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='appointment',
            name='participants',
            field=models.ManyToManyField(to='api.Participant'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acceptedoption',
            name='option',
            field=models.ForeignKey(to='api.ScheduleOption'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='acceptedoption',
            name='participant',
            field=models.ForeignKey(related_name='possible_options', to='api.Participant'),
            preserve_default=True,
        ),
    ]

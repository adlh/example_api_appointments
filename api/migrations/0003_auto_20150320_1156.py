# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20150317_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceptedoption',
            name='participant',
            field=models.ForeignKey(related_name='accepted_options', to='api.Participant'),
            preserve_default=True,
        ),
    ]

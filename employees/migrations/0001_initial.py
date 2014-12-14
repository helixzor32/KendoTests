# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('dob', models.DateTimeField(verbose_name='date of birth')),
                ('age', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

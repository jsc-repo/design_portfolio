# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-01 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='img_name',
            field=models.CharField(default='image_name', max_length=200),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images'),
        ),
    ]

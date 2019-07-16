# Generated by Django 2.2.2 on 2019-07-09 16:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20190709_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='area',
            field=models.FloatField(blank=False, null=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='floor',
            field=models.IntegerField(blank=False, null=False),
            preserve_default=False,
        ),
    ]

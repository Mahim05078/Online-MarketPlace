# Generated by Django 2.2.2 on 2019-07-09 16:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_shop_shopname'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='area',
            field=models.FloatField(blank=False, null=False),
            preserve_default=False,
        ),
    ]
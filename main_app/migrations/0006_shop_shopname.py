# Generated by Django 2.2.2 on 2019-07-09 16:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20190707_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shopname',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

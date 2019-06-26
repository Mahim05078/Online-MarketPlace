# Generated by Django 2.2.2 on 2019-06-26 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cust_dob',
            field=models.DateField(),
        ),
        migrations.CreateModel(
            name='RequestedRent',
            fields=[
                ('NID', models.TextField(primary_key=True, serialize=False)),
                ('is_granted', models.IntegerField()),
                ('paid', models.IntegerField()),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('mobile', models.TextField()),
                ('address', models.TextField()),
                ('shop_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Shop')),
            ],
        ),
    ]

# Generated by Django 3.2.9 on 2022-04-07 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gstapi', '0002_customer_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gst',
            field=models.IntegerField(default=0),
        ),
    ]

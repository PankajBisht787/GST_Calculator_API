# Generated by Django 3.2.9 on 2022-04-07 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gstapi', '0003_customer_gst'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='State',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='State_code',
            new_name='state_code',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='gst',
        ),
    ]

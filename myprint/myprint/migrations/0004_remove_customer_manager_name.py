# Generated by Django 4.1.1 on 2022-10-13 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprint', '0003_rename_price_with_vat_orderform_total_price_with_vat_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='manager_name',
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-13 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprint', '0002_remove_orderform_price_free_vat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderform',
            old_name='price_with_VAT',
            new_name='total_price_with_VAT',
        ),
        migrations.RemoveField(
            model_name='orderform',
            name='total',
        ),
    ]

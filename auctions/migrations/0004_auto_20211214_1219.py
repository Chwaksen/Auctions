# Generated by Django 3.2.9 on 2021-12-14 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='listing',
            name='starting_bid',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
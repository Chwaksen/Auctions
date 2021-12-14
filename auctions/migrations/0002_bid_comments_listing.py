# Generated by Django 3.2.9 on 2021-12-14 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('descr', models.TextField()),
                ('starting_bid', models.IntegerField()),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('close_date', models.DateField(auto_now=True)),
                ('status', models.BooleanField()),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_listings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_comments', to=settings.AUTH_USER_MODEL)),
                ('listing_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='l_comments', to='auctions.listing')),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='u_bids', to=settings.AUTH_USER_MODEL)),
                ('listing_bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='l_bids', to='auctions.listing')),
            ],
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-15 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0025_offer_min_delivery_time_offer_min_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='min_delivery_time',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='offer',
            name='min_price',
            field=models.CharField(default='', max_length=255),
        ),
    ]

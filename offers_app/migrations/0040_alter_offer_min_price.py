# Generated by Django 5.1.3 on 2024-12-23 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0039_offer_max_delivery_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='min_price',
            field=models.FloatField(blank=True, max_length=255),
        ),
    ]
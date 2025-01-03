# Generated by Django 5.1.3 on 2024-12-15 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0024_remove_offer_details_offer_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='min_delivery_time',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='min_price',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offer',
            name='user_details',
            field=models.JSONField(default=list),
        ),
    ]

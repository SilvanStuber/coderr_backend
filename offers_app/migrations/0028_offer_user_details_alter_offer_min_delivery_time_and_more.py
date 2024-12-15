# Generated by Django 5.1.3 on 2024-12-15 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0027_remove_offer_user_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='user_details',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='offer',
            name='min_delivery_time',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='offer',
            name='min_price',
            field=models.CharField(max_length=255),
        ),
    ]

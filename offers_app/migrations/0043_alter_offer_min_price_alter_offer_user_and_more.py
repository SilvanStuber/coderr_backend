# Generated by Django 5.1.3 on 2024-12-23 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0042_alter_offer_min_price_alter_offerdetail_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='min_price',
            field=models.FloatField(blank=True, default=0.0, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='offer',
            name='user',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='offerdetail',
            name='user',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

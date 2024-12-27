# Generated by Django 5.1.3 on 2024-12-27 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0065_alter_offer_min_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='min_price',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]

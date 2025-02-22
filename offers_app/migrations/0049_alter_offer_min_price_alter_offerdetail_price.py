# Generated by Django 5.1.3 on 2024-12-26 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0048_alter_offerdetail_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='min_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='offerdetail',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]

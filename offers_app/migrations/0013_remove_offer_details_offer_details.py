# Generated by Django 5.1.3 on 2024-12-15 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0012_remove_offer_details_offer_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='details',
        ),
        migrations.AddField(
            model_name='offer',
            name='details',
            field=models.ManyToManyField(related_name='offers', to='offers_app.offerdetail'),
        ),
    ]
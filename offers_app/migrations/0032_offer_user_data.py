# Generated by Django 5.1.3 on 2024-12-15 16:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0031_alter_offer_image_alter_offer_min_delivery_time_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='user_data',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, related_name='created_tasks', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]

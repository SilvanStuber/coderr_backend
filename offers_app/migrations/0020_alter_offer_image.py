# Generated by Django 5.1.3 on 2024-12-15 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0019_remove_offer_details_alter_offer_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]

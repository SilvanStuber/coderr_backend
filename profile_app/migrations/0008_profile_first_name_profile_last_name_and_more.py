# Generated by Django 5.1.3 on 2024-12-08 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0007_remove_profile_first_name_remove_profile_last_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

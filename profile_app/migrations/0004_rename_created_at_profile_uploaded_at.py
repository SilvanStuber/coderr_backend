# Generated by Django 5.1.3 on 2024-12-08 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='created_at',
            new_name='uploaded_at',
        ),
    ]

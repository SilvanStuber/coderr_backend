# Generated by Django 5.1.3 on 2024-12-21 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0018_delete_profilebusiness_delete_profilecustomer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.IntegerField(),
        ),
    ]
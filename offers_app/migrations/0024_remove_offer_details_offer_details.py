# Generated by Django 5.1.3 on 2024-12-15 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers_app', '0023_alter_offerdetail_revisions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offer',
            name='details',
        ),
        migrations.AddField(
            model_name='offer',
            name='details',
            field=models.JSONField(default=list),
        ),
    ]

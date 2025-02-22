# Generated by Django 5.1.3 on 2024-12-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0010_alter_profile_description_alter_profile_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default='uu', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='uu', max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='uuu', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='uuu', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='uuu', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tel',
            field=models.CharField(default='uu', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.CharField(default='uu', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(default='iuuu', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='working_hours',
            field=models.CharField(default='uu', max_length=50, null=True),
        ),
    ]

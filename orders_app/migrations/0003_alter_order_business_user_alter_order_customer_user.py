# Generated by Django 5.1.3 on 2024-12-21 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders_app', '0002_alter_order_business_user_alter_order_customer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='business_user',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_user',
            field=models.IntegerField(),
        ),
    ]

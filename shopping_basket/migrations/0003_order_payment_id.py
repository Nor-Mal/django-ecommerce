# Generated by Django 3.1.7 on 2021-08-07 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_basket', '0002_order_total_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

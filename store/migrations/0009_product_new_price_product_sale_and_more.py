# Generated by Django 5.0.4 on 2024-04-28 18:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='new_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(verbose_name=datetime.datetime(2024, 4, 28, 20, 55, 19, 729846)),
        ),
    ]

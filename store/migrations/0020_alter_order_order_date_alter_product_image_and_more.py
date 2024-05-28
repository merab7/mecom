# Generated by Django 5.0.4 on 2024-04-29 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_rename_mimage_1_product_model_image_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(verbose_name=datetime.datetime(2024, 4, 29, 19, 7, 17, 385590)),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='uploads/products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='model_image_1',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='uploads/products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='model_image_2',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='uploads/products'),
        ),
    ]

# Generated by Django 5.0.2 on 2024-05-14 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_profile_city_profile_zipcode_alter_profile_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='old_cart',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

# Generated by Django 5.0.2 on 2024-02-15 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0011_reservation_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='quantity_available',
            field=models.IntegerField(default=0),
        ),
    ]
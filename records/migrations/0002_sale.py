# Generated by Django 5.0.2 on 2024-02-13 15:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_sold', models.PositiveIntegerField()),
                ('sale_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sale_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.product')),
            ],
        ),
    ]

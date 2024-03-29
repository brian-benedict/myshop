# Generated by Django 5.0.2 on 2024-02-15 12:43

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0007_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservationPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_paid', models.DateField(default=django.utils.timezone.now)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='records.reservation')),
            ],
        ),
    ]

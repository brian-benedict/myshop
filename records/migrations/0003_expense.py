# Generated by Django 5.0.2 on 2024-02-13 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_sale'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expense_date', models.DateField()),
            ],
        ),
    ]

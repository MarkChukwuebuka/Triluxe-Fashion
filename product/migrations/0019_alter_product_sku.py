# Generated by Django 5.0.7 on 2025-01-25 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_remove_dealoftheday_number_of_available_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default='001', editable=False, max_length=255, unique=True),
        ),
    ]

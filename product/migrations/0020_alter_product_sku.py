# Generated by Django 5.0.7 on 2025-01-25 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0019_alter_product_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(editable=False, max_length=255, unique=True),
        ),
    ]

# Generated by Django 5.0.7 on 2024-12-19 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0010_alter_payment_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=255)),
                ('account_name', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=255)),
            ],
        ),
    ]

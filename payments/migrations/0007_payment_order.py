# Generated by Django 5.0.7 on 2024-08-25 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_alter_order_options_remove_order_amount_paid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='payments.order'),
        ),
    ]
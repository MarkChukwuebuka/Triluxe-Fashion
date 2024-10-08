# Generated by Django 5.0.7 on 2024-08-22 09:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_remove_profile_address2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='role',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]

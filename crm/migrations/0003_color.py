# Generated by Django 5.0.7 on 2024-10-06 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_delete_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hex_code', models.CharField(blank=True, max_length=7, null=True)),
            ],
        ),
    ]
# Generated by Django 5.0.7 on 2024-08-09 19:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cover_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='cover image'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image3'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image4'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image5',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image5'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image6',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image6'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-12-27 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productdescri',
            field=models.CharField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='subdescription',
            field=models.TextField(blank=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='subcatmodel',
            name='modeldescription',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]

# Generated by Django 3.2.8 on 2021-12-27 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='categoryname',
            field=models.ForeignKey(default='', max_length=100, on_delete=django.db.models.deletion.CASCADE, to='inventory.category'),
        ),
    ]
# Generated by Django 3.2.8 on 2022-01-02 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_alter_ordersupply_arrivedat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordersupply',
            name='arrivedat',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
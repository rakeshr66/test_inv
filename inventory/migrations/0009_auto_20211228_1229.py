# Generated by Django 3.2.8 on 2021-12-28 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_auto_20211228_1227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcatmodel',
            old_name='brandname',
            new_name='branname',
        ),
        migrations.RenameField(
            model_name='subcatmodel',
            old_name='subcatname',
            new_name='subcatename',
        ),
    ]
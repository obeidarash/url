# Generated by Django 3.2.4 on 2022-08-01 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0005_auto_20220801_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='ip',
            field=models.GenericIPAddressField(verbose_name='Ip Address'),
        ),
    ]
# Generated by Django 2.2.3 on 2020-06-15 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='total_price',
        ),
    ]

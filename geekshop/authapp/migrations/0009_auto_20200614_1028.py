# Generated by Django 2.2.3 on 2020-06-14 07:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0008_auto_20200610_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 16, 7, 28, 14, 180964, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
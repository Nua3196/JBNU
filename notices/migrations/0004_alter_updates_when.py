# Generated by Django 4.2.3 on 2023-08-04 02:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0003_updates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updates',
            name='when',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 4, 2, 41, 51, 717853, tzinfo=datetime.timezone.utc)),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-04 02:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notices', '0004_alter_updates_when'),
    ]

    operations = [
        migrations.AlterField(
            model_name='updates',
            name='when',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

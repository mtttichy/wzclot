# Generated by Django 2.1.4 on 2020-01-28 22:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wlct', '0063_auto_20200128_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentgame',
            name='game_start_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

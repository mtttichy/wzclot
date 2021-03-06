# Generated by Django 2.1.4 on 2019-07-10 16:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wlct', '0031_merge_20190710_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentgameentry',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tournamentgameentry',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]

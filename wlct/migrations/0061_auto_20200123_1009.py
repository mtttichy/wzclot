# Generated by Django 2.1.4 on 2020-01-23 18:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wlct', '0060_auto_20200122_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealTimeLadderVeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ladder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wlct.RealTimeLadder')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wlct.TournamentTeam')),
                ('template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wlct.RealTimeLadderTemplate')),
            ],
        ),
        migrations.AlterField(
            model_name='tournamentgame',
            name='game_start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 23, 18, 9, 31, 844920)),
        ),
    ]

# Generated by Django 2.1.4 on 2019-01-22 18:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wlct', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentgame',
            name='winning_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wlct.TournamentTeam'),
        ),
    ]

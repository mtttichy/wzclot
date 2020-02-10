# Generated by Django 2.1.4 on 2020-01-19 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wlct', '0055_player_discord_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentgame',
            name='needs_recreation',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='tournamentgame',
            name='winning_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='wlct.TournamentTeam'),
        ),
    ]

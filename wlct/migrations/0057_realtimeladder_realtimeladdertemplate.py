# Generated by Django 2.1.4 on 2020-01-20 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wlct', '0056_auto_20200119_0829'),
    ]

    operations = [
        migrations.CreateModel(
            name='RealTimeLadder',
            fields=[
                ('tournament_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wlct.Tournament')),
                ('direct_seconds_per_turn', models.IntegerField(blank=True, default=180, null=True)),
                ('auto_boot_seconds', models.IntegerField(blank=True, default=180, null=True)),
                ('seconds_banked', models.IntegerField(blank=True, default=480, null=True)),
            ],
            bases=('wlct.tournament',),
        ),
        migrations.CreateModel(
            name='RealTimeLadderTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template', models.IntegerField(blank=True, db_index=True, default=0, null=True)),
                ('name', models.CharField(blank=True, default='My Template Name', max_length=255, null=True)),
                ('ladder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wlct.RealTimeLadder')),
            ],
        ),
    ]

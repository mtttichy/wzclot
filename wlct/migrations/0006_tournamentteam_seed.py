# Generated by Django 2.1.4 on 2019-03-05 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wlct', '0005_auto_20190130_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentteam',
            name='seed',
            field=models.IntegerField(default=0),
        ),
    ]

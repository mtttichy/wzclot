# Generated by Django 2.1.4 on 2019-05-17 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wlct', '0014_auto_20190516_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='roundrobintournament',
            name='parent_tournament',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rr_parent', to='wlct.Tournament'),
        ),
    ]

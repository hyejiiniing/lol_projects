# Generated by Django 5.0.6 on 2024-07-14 01:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("riot_app", "0008_player"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="player",
            name="position_icon",
        ),
        migrations.RemoveField(
            model_name="player",
            name="team_logo",
        ),
    ]

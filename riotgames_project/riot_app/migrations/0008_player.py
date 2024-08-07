# Generated by Django 5.0.6 on 2024-07-05 02:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("riot_app", "0007_remove_championskin_champion_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Player",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("team_logo", models.URLField()),
                ("team_name", models.CharField(max_length=100)),
                ("position_icon", models.CharField(max_length=100)),
                ("position_name", models.CharField(max_length=10)),
                ("player_photo", models.URLField()),
                ("player_name", models.CharField(max_length=100)),
            ],
        ),
    ]

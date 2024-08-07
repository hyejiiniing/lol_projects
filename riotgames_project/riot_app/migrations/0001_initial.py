# Generated by Django 5.0.6 on 2024-07-01 08:53

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Match",
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
                ("team_a_name", models.CharField(max_length=100)),
                ("team_b_name", models.CharField(max_length=100)),
                ("team_a_logo", models.URLField(default="default_logo_url")),
                ("team_b_logo", models.URLField(default="default_logo_url")),
                ("match_date", models.CharField(max_length=100)),
                ("match_time", models.CharField(max_length=100)),
                ("vs_image", models.TextField()),
            ],
        ),
    ]

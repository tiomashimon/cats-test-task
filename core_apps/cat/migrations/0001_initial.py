# Generated by Django 4.2.5 on 2024-01-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cat",
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
                ("cat_id", models.CharField(max_length=50)),
                ("url", models.CharField(max_length=255)),
            ],
        ),
    ]

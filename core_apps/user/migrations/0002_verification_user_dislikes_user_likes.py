# Generated by Django 4.2.5 on 2024-01-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Verification",
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
                ("email", models.EmailField(max_length=254)),
                ("code", models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="dislikes",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="user",
            name="likes",
            field=models.IntegerField(default=0),
        ),
    ]

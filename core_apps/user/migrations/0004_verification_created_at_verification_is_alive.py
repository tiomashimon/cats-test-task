# Generated by Django 4.2.5 on 2024-01-06 17:31

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0003_verification_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="verification",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime(
                    2024, 1, 6, 17, 31, 26, 124909, tzinfo=datetime.timezone.utc
                ),
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="verification",
            name="is_alive",
            field=models.BooleanField(default=True),
        ),
    ]

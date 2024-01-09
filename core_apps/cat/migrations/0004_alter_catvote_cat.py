# Generated by Django 4.2.5 on 2024-01-09 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("cat", "0003_catvote"),
    ]

    operations = [
        migrations.AlterField(
            model_name="catvote",
            name="cat",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="votes_received",
                to="cat.cat",
            ),
        ),
    ]

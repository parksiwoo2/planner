# Generated by Django 4.2.16 on 2025-03-08 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("plan", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="time",
            field=models.CharField(default="00:00:00", max_length=100),
        ),
    ]

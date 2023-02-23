# Generated by Django 4.1.7 on 2023-02-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="access_token",
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="refresh_token",
            field=models.CharField(max_length=256, null=True),
        ),
    ]

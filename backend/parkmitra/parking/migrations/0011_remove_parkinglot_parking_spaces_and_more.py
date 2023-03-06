# Generated by Django 4.1.7 on 2023-03-06 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("parking", "0010_alter_vehicle_owner"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="parkinglot",
            name="parking_spaces",
        ),
        migrations.AddField(
            model_name="parkingspace",
            name="parking_lot",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="parking.parkinglot",
            ),
        ),
        migrations.AlterField(
            model_name="parkingsession",
            name="parking_space",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sessions",
                to="parking.parkingspace",
            ),
        ),
        migrations.AlterField(
            model_name="parkingsession",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sessions",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="parkingsession",
            name="vehicle",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sessions",
                to="parking.vehicle",
            ),
        ),
    ]

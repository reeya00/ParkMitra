# Generated by Django 4.1.7 on 2023-02-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "parking",
            "0004_parkingspace_parking_lot_alter_vehicle_vehicle_type_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="parkingsession",
            name="parking_spot",
            field=models.CharField(max_length=64),
        ),
    ]

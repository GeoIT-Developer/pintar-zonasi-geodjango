# Generated by Django 5.1.3 on 2024-11-28 10:43

import django.contrib.gis.db.models.fields
import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SekolahMetadata",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("level", models.CharField(max_length=50)),
                ("type", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=255)),
                (
                    "bbox",
                    django.contrib.gis.db.models.fields.PolygonField(
                        blank=True, null=True, srid=4326
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "tb_sekolah_metadata",
            },
        ),
        migrations.CreateModel(
            name="Sekolah",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("tipe", models.CharField(blank=True, default="", max_length=50)),
                ("npsn", models.CharField(blank=True, default="", max_length=50)),
                ("alamat", models.CharField(blank=True, default="", max_length=255)),
                ("kuota", models.IntegerField(blank=True, default=0)),
                (
                    "keterangan",
                    models.CharField(blank=True, default="", max_length=255),
                ),
                ("lat", models.FloatField(blank=True, null=True)),
                ("lon", models.FloatField(blank=True, null=True)),
                ("point", django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "file_metadata",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sekolah",
                        to="sekolah.sekolahmetadata",
                    ),
                ),
            ],
            options={
                "db_table": "tb_sekolah",
            },
        ),
    ]
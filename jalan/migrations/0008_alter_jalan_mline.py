# Generated by Django 5.1.3 on 2024-12-06 21:55

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jalan", "0007_alter_jalan_cost"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jalan",
            name="mline",
            field=django.contrib.gis.db.models.fields.LineStringField(srid=4326),
        ),
    ]
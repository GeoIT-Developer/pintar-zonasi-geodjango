# Generated by Django 5.1.3 on 2024-12-06 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jalan", "0005_jalanmetadata_topology_status"),
    ]

    operations = [
        migrations.RenameField(
            model_name="jalanmetadata",
            old_name="status",
            new_name="data_status",
        ),
        migrations.RemoveField(
            model_name="jalan",
            name="fclass",
        ),
        migrations.RemoveField(
            model_name="jalan",
            name="name",
        ),
        migrations.RemoveField(
            model_name="jalan",
            name="osm_id",
        ),
    ]

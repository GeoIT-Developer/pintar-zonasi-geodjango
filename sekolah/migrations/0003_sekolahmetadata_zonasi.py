# Generated by Django 5.1.3 on 2024-12-10 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sekolah", "0002_sekolah_nama"),
    ]

    operations = [
        migrations.AddField(
            model_name="sekolahmetadata",
            name="zonasi",
            field=models.BooleanField(default=False),
        ),
    ]
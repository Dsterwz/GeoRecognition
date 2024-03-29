# Generated by Django 5.0 on 2024-01-08 18:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TempImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=500, null=True)),
                ("image", models.ImageField(upload_to="tmp")),
                ("desc", models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-23 15:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("volunteers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Cat",
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
                ("name", models.CharField(max_length=200)),
                ("address", models.CharField(max_length=200)),
                ("city", models.CharField(max_length=200)),
                ("description", models.TextField(blank=True)),
                ("donation", models.IntegerField()),
                ("age", models.IntegerField()),
                ("vaccinated", models.BooleanField(default=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "male"), ("female", "female")], max_length=10
                    ),
                ),
                ("breed", models.CharField(max_length=200)),
                ("photo_main", models.ImageField(upload_to="photos/%Y/%m/%d/")),
                (
                    "photo_1",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                (
                    "photo_2",
                    models.ImageField(blank=True, upload_to="photos/%Y/%m/%d/"),
                ),
                ("is_published", models.BooleanField(default=True)),
                (
                    "list_date",
                    models.DateTimeField(blank=True, default=datetime.datetime.now),
                ),
                (
                    "volunteer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="volunteers.volunteer",
                    ),
                ),
            ],
        ),
    ]

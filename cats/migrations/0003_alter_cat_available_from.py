# Generated by Django 4.1.1 on 2022-09-29 12:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cats", "0002_cat_available_from"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cat",
            name="available_from",
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]

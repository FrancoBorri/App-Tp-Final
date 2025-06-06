# Generated by Django 5.2.1 on 2025-05-09 19:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="User_profile",
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
                ("address", models.TextField()),
                ("phone", models.CharField(blank=True, max_length=15, null=True)),
                (
                    "picture_profile",
                    models.ImageField(blank=True, null=True, upload_to="profile_pics/"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User Profile",
                "verbose_name_plural": "User Profiles",
                "db_table": "user_profile",
                "ordering": ["user"],
            },
        ),
    ]

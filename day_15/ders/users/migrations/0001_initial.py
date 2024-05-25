# Generated by Django 5.0.3 on 2024-04-21 17:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="user",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "phone_number",
                    models.CharField(max_length=12, verbose_name="Telefon Numarası"),
                ),
                ("address", models.TextField(max_length=1000, verbose_name="Adres")),
                ("activate", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Kullanıcı Profili",
                "verbose_name_plural": "Kullanıcı Profilleri",
            },
        ),
    ]
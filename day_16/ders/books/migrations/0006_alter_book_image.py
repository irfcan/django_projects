# Generated by Django 5.0.3 on 2024-04-20 19:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0005_book_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="image",
            field=models.ImageField(default="", upload_to="image"),
        ),
    ]
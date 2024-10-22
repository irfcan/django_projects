# Generated by Django 5.0.3 on 2024-04-19 21:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0003_remove_book_author_book_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="slug",
            field=models.SlugField(
                blank=True,
                default=None,
                editable=False,
                max_length=100,
                null=True,
                unique=True,
            ),
        ),
    ]

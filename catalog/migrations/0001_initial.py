# Generated by Django 4.2.4 on 2023-09-07 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                (
                    "category_name",
                    models.CharField(max_length=100, verbose_name="Наименование"),
                ),
                ("description", models.TextField(verbose_name="Описание")),
            ],
            options={
                "verbose_name": "категория",
                "verbose_name_plural": "категории",
            },
        ),
        migrations.CreateModel(
            name="Contacts",
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
                ("contact_name", models.CharField(max_length=100, verbose_name="Имя")),
                ("ph_number", models.IntegerField(verbose_name="Телефон")),
                ("message", models.TextField(verbose_name="Сообщение")),
            ],
            options={
                "verbose_name": "контакт",
                "verbose_name_plural": "контакты",
            },
        ),
        migrations.CreateModel(
            name="Product",
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
                (
                    "product_name",
                    models.CharField(max_length=100, verbose_name="Наименование"),
                ),
                ("descriptions", models.TextField(verbose_name="Описание")),
                (
                    "picture",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="product/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, verbose_name="Цена за покупку"
                    ),
                ),
                (
                    "date_create",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "date_update",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата последнего изменения"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
            },
        ),
    ]

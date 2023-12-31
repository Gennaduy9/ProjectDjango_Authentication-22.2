# Generated by Django 4.2.5 on 2023-09-19 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "permissions": [
                    (
                        "can_change_is_published_permission",
                        "Can cancel product publication",
                    ),
                    ("can_change_desc_permission", "Can change product description"),
                    ("can_change_category_permission", "Can change product category"),
                ],
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
            },
        ),
        migrations.AddField(
            model_name="product",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
    ]

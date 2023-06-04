# Generated by Django 4.2.1 on 2023-06-04 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("provider", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "baseusermodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="provider.baseusermodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Cliente",
            },
            bases=("provider.baseusermodel",),
        ),
        migrations.CreateModel(
            name="Seller",
            fields=[
                (
                    "baseusermodel_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="provider.baseusermodel",
                    ),
                ),
            ],
            options={
                "verbose_name": "Vendedor",
                "verbose_name_plural": "Vendedores",
            },
            bases=("provider.baseusermodel",),
        ),
    ]
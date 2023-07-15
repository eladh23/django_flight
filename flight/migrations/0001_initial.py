# Generated by Django 4.2.3 on 2023-07-15 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Flight",
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
                ("source", models.CharField(max_length=100)),
                ("destination", models.CharField(max_length=100)),
                ("tickets", models.IntegerField()),
                ("airline", models.CharField(max_length=100)),
                ("date", models.DateField()),
            ],
        ),
    ]
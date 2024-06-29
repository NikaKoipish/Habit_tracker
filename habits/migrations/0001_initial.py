# Generated by Django 5.0.6 on 2024-06-22 19:19

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
            name="NiceHabit",
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
                ("name", models.CharField(verbose_name="Название приятной привычки")),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание приятной привычки"
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="создатель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Приятная привычка",
                "verbose_name_plural": "Приятные привычки",
            },
        ),
        migrations.CreateModel(
            name="Reward",
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
                ("name", models.CharField(verbose_name="Название вознаграждения")),
                (
                    "owner",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="создатель",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вознаграждение",
                "verbose_name_plural": "Вознаграждения",
            },
        ),
        migrations.CreateModel(
            name="Habit",
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
                ("name", models.CharField(verbose_name="Название привычки")),
                (
                    "description",
                    models.TextField(
                        blank=True, null=True, verbose_name="Описание привычки"
                    ),
                ),
                (
                    "place",
                    models.TextField(blank=True, null=True, verbose_name="место"),
                ),
                ("time", models.TimeField(blank=True, null=True, verbose_name="время")),
                (
                    "is_nice",
                    models.BooleanField(
                        default=True, verbose_name="признак приятной привычки"
                    ),
                ),
                ("periodicity", models.IntegerField(default=1)),
                ("time_to_implement", models.IntegerField(default=120)),
                ("is_public", models.BooleanField(default=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="создатель",
                    ),
                ),
                (
                    "related_nice_habit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.nicehabit",
                        verbose_name="связанная привычка",
                    ),
                ),
                (
                    "reward",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.reward",
                        verbose_name="вознаграждение",
                    ),
                ),
            ],
            options={
                "verbose_name": "Привычка",
                "verbose_name_plural": "Привычки",
            },
        ),
    ]

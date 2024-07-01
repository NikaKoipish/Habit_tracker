# Generated by Django 5.0.6 on 2024-07-01 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("habits", "0006_alter_habit_action_alter_habit_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="habit",
            name="periodicity",
            field=models.PositiveIntegerField(
                default=1,
                help_text="Укажите периодичность от 1 до 7, где 1 - один раз в неделю, а 7 - это каждый день",
            ),
        ),
    ]

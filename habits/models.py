from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}


class Reward(models.Model):
    """Модель вознаграждения"""

    name = models.CharField(verbose_name="Название вознаграждения")
    owner = models.ForeignKey(
        User, verbose_name="создатель", on_delete=models.SET_NULL, **NULLABLE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Вознаграждение"
        verbose_name_plural = "Вознаграждения"


class Habit(models.Model):
    """Модель привычки"""

    owner = models.ForeignKey(
        User, verbose_name="создатель", on_delete=models.CASCADE, **NULLABLE
    )
    name = models.CharField(
        verbose_name="Название привычки",
        help_text="Назовите свою привычку(например, 'Спортзал')",
    )
    action = models.TextField(
        verbose_name="Действие",
        help_text="Опишите действие по примеру: 'ходить в спортзал'",
    )
    place = models.TextField(
        verbose_name="место",
        help_text="Укажите место по примеру: 'спортзал'",
        **NULLABLE,
    )
    time = models.TimeField(
        verbose_name="время",
        help_text="Укажите время по примеру: '18:00:00'",
        default="18:00:00",
    )
    is_nice = models.BooleanField(
        default=False, verbose_name="признак приятной привычки"
    )
    related_nice_habit = models.ForeignKey(
        "self", verbose_name="связанная привычка", on_delete=models.SET_NULL, **NULLABLE
    )
    periodicity = models.PositiveIntegerField(
        default=1,
        help_text="Укажите периодичность от 1 до 7, где 1 - один раз в неделю, а 7 - это каждый день",
    )  # 1 день
    reward = models.ForeignKey(
        Reward, verbose_name="вознаграждение", on_delete=models.SET_NULL, **NULLABLE
    )
    time_to_implement = models.IntegerField(default=120)  # 2 минуты(120 секунд)
    is_public = models.BooleanField(default=True)
    send_date = models.DateField(
        auto_now_add=True, verbose_name="дата начала отправки", **NULLABLE
    )

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

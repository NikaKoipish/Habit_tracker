from django.db import models

from users.models import User

NULLABLE = {"null": True, "blank": True}


class NiceHabit(models.Model):
    """Модель приятной привычки"""

    name = models.CharField(verbose_name="Название приятной привычки")
    description = models.TextField(
        verbose_name="Описание приятной привычки", **NULLABLE
    )
    owner = models.ForeignKey(
        User, verbose_name="создатель", on_delete=models.SET_NULL, **NULLABLE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Приятная привычка"
        verbose_name_plural = "Приятные привычки"


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

    owner = models.ForeignKey(User, verbose_name="создатель", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название привычки")
    description = models.TextField(verbose_name="Описание привычки", **NULLABLE)
    place = models.TextField(verbose_name="место", **NULLABLE)
    time = models.TimeField(verbose_name="время", **NULLABLE)
    is_nice = models.BooleanField(
        default=True, verbose_name="признак приятной привычки"
    )
    related_nice_habit = models.ForeignKey(
        NiceHabit,
        verbose_name="связанная привычка",
        on_delete=models.SET_NULL,
        **NULLABLE
    )
    periodicity = models.IntegerField(default=1)  # 1 день
    reward = models.ForeignKey(
        Reward, verbose_name="вознаграждение", on_delete=models.SET_NULL, **NULLABLE
    )
    time_to_implement = models.IntegerField(default=120)  # 2 минуты(120 секунд)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name, self.description, self.time, self.periodicity

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

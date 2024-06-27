from celery import shared_task

import datetime

from django.utils import timezone

from habits.models import Habit
from habits.services import send_telegram_message


@shared_task
def send_habit():
    habits = Habit.objects.all()
    now = datetime.datetime.now().date()
    for habit in habits:
        tg_chat_id = habit.owner.tg_chat_id
        if habit.send_date == now and habit.reward:
            message = f"Я буду {habit.action} в {habit.time} в {habit.place} и получу за это {habit.reward.name}"
            send_telegram_message(message, tg_chat_id)
            periodicity = habit.periodicity
            habit.send_date += datetime.timedelta(days=periodicity)
        elif habit.send_date == now and habit.related_nice_habit:
            message = f"Я буду {habit.action} в {habit.time} в {habit.place} и получу за это {habit.related_nice_habit.name}"
            send_telegram_message(message, tg_chat_id)
            periodicity = habit.periodicity
            habit.send_date += datetime.timedelta(days=periodicity)

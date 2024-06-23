from rest_framework import serializers


class DurationValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value).get(self.field)
        if val and val > 120:
            raise serializers.ValidationError(f"{self.field} не должно превышать 120 секунд")


class PeriodicityValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        val = dict(value).get(self.field)
        if val and val > 7:
            raise serializers.ValidationError(f"{self.field} не должно быть больше 7")


class NiceHabitRewardValidator:
    requires_context = True

    def __init__(self, field):
        self.field = field

    def __call__(self, value, serializer_field):
        val = dict(value).get(self.field)
        serializer_field = serializer_field.HabitSerializer.get("reward")
        if val and serializer_field:
            raise serializers.ValidationError("Выберите или приятную привычку, или вознаграждение")

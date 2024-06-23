from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet

from habits.models import Habit, NiceHabit, Reward
from habits.validators import DurationValidator, PeriodicityValidator, NiceHabitRewardValidator


class HabitSerializer(ModelSerializer):

    class Meta:
        model = Habit
        fields = "__all__"
        read_only_fields = ("id", "owner")
        validators = [DurationValidator(field="time_to_implement"), PeriodicityValidator(field="periodicity"), NiceHabitRewardValidator(field="related_nice_habit")]


class NiceHabitSerializer(ModelSerializer):
    habits = HabitSerializer(many=True, read_only=True)
    class Meta:
        model = NiceHabit
        fields = "__all__"


class RewardSerializer(ModelSerializer):
    habits = HabitSerializer(many=True, read_only=True)
    class Meta:
        model = Reward
        fields = "__all__"


class NiceHabitViewSet(ModelViewSet):
    queryset = NiceHabit.objects.all()
    serializer_class = NiceHabitSerializer


class RewardViewSet(ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer

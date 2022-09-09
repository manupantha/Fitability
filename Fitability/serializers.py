from rest_framework import serializers
from .models import User, WorkOut, WorkOutRoutine, Exercise, DayEntry


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class WorkOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOut
        fields = '__all__'


class WorkOutRoutineSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOutRoutine
        fields = '__all__'


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'


class DayEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DayEntry
        fields = '__all__'

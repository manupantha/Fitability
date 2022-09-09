from rest_framework import generics
from .models import Exercise, User, WorkOut, WorkOutRoutine, DayEntry

from .serializers import UserSerializer, WorkOutSerializer, WorkOutRoutineSerializer, \
    DayEntrySerializer, ExerciseSerializer


class UserList(generics.ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        user_id = self.request.query_params.get('user_id')
        if user_id is not None:
            queryset = queryset.filter(entry_id=user_id)
        return queryset


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class WorkOutRoutineList(generics.ListCreateAPIView):
    serializer_class = WorkOutRoutineSerializer
    queryset = WorkOutRoutine.objects.all()


class WorkOutRoutineDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkOutRoutineSerializer
    queryset = WorkOutRoutine.objects.all()


class ExerciseList(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        queryset = Exercise.objects.all()
        workoutroutine = self.request.query_params.get('workoutroutine')
        if workoutroutine is not None:
            queryset = queryset.filter(movement=WorkOutRoutine)
        return queryset


class ExerciseDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()


class WorkOutList(generics.ListCreateAPIView):
    serializer_class = WorkOutSerializer

    def get_queryset(self):
        queryset = WorkOut.objects.all()
        exercise = self.request.query_params.get('exercise')
        if exercise is not None:
            queryset = queryset.filter(exercise=exercise)
        return queryset


class WorkOutDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkOutSerializer
    queryset = WorkOut.objects.all()


class DayEntryList(generics.ListCreateAPIView):
    serializer_class = DayEntrySerializer

    def get_queryset(self):
        queryset = DayEntry.objects.all()
        userid = self.request.query_params.get('userid')
        workoutroutine=self.request.query_params.get('workoutroutine')
        workout=self.request.query_params.get('workout')
        if userid is not None:
            queryset = queryset.filter(entry_id=userid)

        if workoutroutine is not None:
            queryset=queryset.filter(work_out_routine=workoutroutine)

        if workout is not None:
            queryset=queryset.filter(work_out=workout)

        return queryset


class DayEntryDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DayEntrySerializer
    queryset = DayEntry.objects.all()

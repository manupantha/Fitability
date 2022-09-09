from django.urls import path
from .views import UserList, UserDetails,WorkOutList,WorkOutDetails,WorkOutRoutineList,WorkOutRoutineDetails
from .views import ExerciseList,ExerciseDetails,DayEntryList,DayEntryDetails

urlpatterns = [
    path('user/', UserList.as_view()),
    path('user/<int:pk>/', UserDetails.as_view()),
    path('workout/',WorkOutList.as_view()),
    path('workout/<int:pk>/',WorkOutDetails.as_view()),
    path('workoutroutine/',WorkOutRoutineList.as_view()),
    path('workoutroutine/<int:pk>/',WorkOutRoutineDetails.as_view()),
    path('exercise/',ExerciseList.as_view()),
    path('exercise/<int:pk>/', ExerciseDetails.as_view()),
    path('dayentry/',DayEntryList.as_view()),
    path('dayentry/<int:pk>/',DayEntryDetails.as_view())
]

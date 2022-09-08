from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    dob = models.DateField(blank=False)
    email = models.EmailField(blank=False)
    contact = models.IntegerField(default=0)
    height = models.IntegerField(default=0)


class WorkOutRoutine(models.Model):
    push = models.CharField(max_length=200)
    pull = models.CharField(max_length=200)
    leg = models.CharField(max_length=200)
    brosplit = models.CharField(max_length=200)


class Exercise(models.Model):
    name = models.CharField(max_length=200)
    movement = models.ForeignKey(WorkOutRoutine, on_delete=models.CASCADE)
    photo = models.TextField(blank=False)


class WorkOut(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    rep = models.IntegerField(default=0)
    sets = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)


class DayEntry(models.Model):
    id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    work_out_routine = models.ForeignKey(WorkOutRoutine, on_delete=models.CASCADE)
    work_out = models.ForeignKey(WorkOut, on_delete=models.CASCADE)

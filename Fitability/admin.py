from django.contrib import admin

from .models  import User,WorkOut,WorkOutRoutine,Exercise,DayEntry

admin.site.register(User)
admin.site.register(WorkOut)
admin.site.register(WorkOutRoutine)
admin.site.register(Exercise)
admin.site.register(DayEntry)

# Register your models here.

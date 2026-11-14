from django.contrib import admin
from .models import Habit, Achieve, Note, Target, Progress

admin.site.register(Habit)
admin.site.register(Achieve)
admin.site.register(Note)
admin.site.register(Target)
admin.site.register(Progress)

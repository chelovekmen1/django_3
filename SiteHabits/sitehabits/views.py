from django.shortcuts import render
from .models import Hamit  # Импортируем твою модель

def habit_list_view(request):
    habits = Hamit.objects.all()
    return render(request, 'tracker.html', {'habits': habits})
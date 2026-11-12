from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import HabitForm
from .models import Habit, Achieve
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.utils import timezone

def my_views(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')
    else:
        form = HabitForm()

        habits = Habit.objects.all()

    return render(request, 'habits.html', {'form': form, 'habits': habits})

def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    habit.delete()
    return redirect('/habits/')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/habits/')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/habits/')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def achievements_view(request):
    achievements = Achieve.objects.filter(user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            Achieve.objects.create(
                user=request.user,
                title=title,
                description=description,
                date=timezone.now().date()
            )
            return redirect('/achievements/')

    return render(request, 'achievements.html', {'achievements': achievements})

def delete_achievement(request, achieve_id):
    achievement = Achieve.objects.filter(id=achieve_id, user=request.user)
    achievement.delete()
    return redirect('/achievements/')
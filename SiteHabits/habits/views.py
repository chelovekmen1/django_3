from re import search

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from .forms import HabitForm
from .models import Habit, Achieve
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.utils import timezone

def my_views(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title:
            Habit.objects.create(
                user = request.user,
                title = title,
                description = description
            )
            return redirect('/habits/')
    search_qwerty = request.GET.get('q', '')
    if search_qwerty:
        habits = Habit.objects.filter(user=request.user, title__icontains=search_qwerty)
    else:
        habits = Habit.objects.filter(user=request.user)


    return render(request, 'habits.html', {'habits': habits, 'search_qwerty': search_qwerty})

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

    search_qwerty = request.GET.get('q', '')

    if search_qwerty:
        achievements = Achieve.objects.filter(user=request.user, title__icontains=search_qwerty)
    else:
        achievements = Achieve.objects.filter(user=request.user)

    return render(request, 'achievements.html', {'achievements': achievements, 'search_qwerty': search_qwerty})

def delete_achievement(request, achieve_id):
    achievement = Achieve.objects.filter(id=achieve_id, user=request.user)
    achievement.delete()
    return redirect('/achievements/')

def logout_view(request):
    logout(request)
    return redirect('/login/')
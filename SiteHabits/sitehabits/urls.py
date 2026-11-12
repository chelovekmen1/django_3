from django.urls import path
from habits.views import my_views, delete_habit, register_view, login_view, achievements_view, delete_achievement

urlpatterns = [
    path('habits/', my_views),
    path('habits/delete/<int:habit_id>/', delete_habit),
    path('register/', register_view),
    path('login/', login_view),
    path('achievements/', achievements_view),
    path('achievements/delete/<int:achieve_id>/', delete_achievement),
]
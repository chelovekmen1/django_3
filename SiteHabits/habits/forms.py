from django import forms
from .models import Habit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['title', 'description']

        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea()
        }

class CustomUserCreationForm(UserCreationForm):
            # Добавляем поле email вручную
    email = forms.EmailField(required=True, label="Email")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']  # Сохраняем email в базу
        if commit:
            user.save()
        return user
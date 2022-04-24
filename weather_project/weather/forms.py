from django import forms
from .models import City, WeatherEvent
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


class WeatherEventForm(forms.ModelForm):
    class Meta:
        model = WeatherEvent
        fields = ['value', 'date', 'time', 'meteo', 'city']
        widgets = {
            'value': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'time': forms.TimeInput(attrs={'class': 'form-control'}),
            'city': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'meteo': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
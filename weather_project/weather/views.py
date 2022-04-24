from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import City, WeatherEvent
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, logout
from .forms import CityForm, UserLoginForm, WeatherEventForm
from .utils import get_plot


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cities')
    else:
        form = UserLoginForm()
    return render(request, 'weather/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def index(request):
    context = {}
    cities = City.objects.all()
    lst = []
    for city in cities:
        qs = WeatherEvent.objects.filter(city__slug=city.slug)
        x = [x.date for x in qs]
        y = [int(y.value) for y in qs]
        chart = get_plot(x, y)
        lst.append(city)
        lst.append(chart)

    return render(request, 'weather/index.html', {'context': lst})


class CityDetailView(DetailView):
    model = City
    template_name = 'weather/city_detail.html'


class CityCreate(CreateView):
    form_class = CityForm
    template_name = 'weather/city_create.html'


class CityUpdate(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'weather/city_update.html'


class CityDelete(DeleteView):
    model = City
    template_name = 'weather/city_delete.html'
    success_url = reverse_lazy('cities')


class WeatherEventDetail(DetailView):
    model = WeatherEvent
    template_name = 'weather/weathereventdetail.html'


class WeatherEventCreate(CreateView):
    model = WeatherEvent
    form_class = WeatherEventForm
    template_name = 'weather/weatherevent_create.html'
    success_url = reverse_lazy('cities')


def get_weather(request, slug):
    city_weather = WeatherEvent.objects.filter(city__slug=slug)
    context = {"city_weather": city_weather}
    return render(request, 'weather/weatherevent_city.html', context=context)




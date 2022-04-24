from django.urls import path
from .views import index, CityDetailView, user_logout, user_login, CityCreate, CityDelete, CityUpdate, \
    WeatherEventDetail, WeatherEventCreate, get_weather

urlpatterns = [
    #path('', CityList.as_view(), name='cities'),
    path('', index, name='cities'),
    path('city/<str:slug>/', CityDetailView.as_view(), name='city_detail'),
    path('city_create/', CityCreate.as_view(), name='city_create'),
    path('city_update/<str:slug>/', CityUpdate.as_view(), name='city_update'),
    path('city_delete/<str:slug>/', CityDelete.as_view(), name='city_delete'),
    path('weathereventdetail/<int:pk>/', WeatherEventDetail.as_view(), name='weathereventdetail'),
    path('weatherevent_create/', WeatherEventCreate.as_view(), name='weatherevent_create'),
    path('weatherevent_city/<str:slug>', get_weather, name='get_weather'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]

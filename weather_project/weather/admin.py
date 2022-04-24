from django.contrib import admin

from .models import WeatherEvent, Meteo, City


class CityInline(admin.TabularInline):
    model = WeatherEvent.city.through
    extra = 1


class MeteoInline(admin.TabularInline):
    model = WeatherEvent.meteo.through
    extra = 1


class WeatherEventAdmin(admin.ModelAdmin):
    list_display = ('value', 'date', 'time', 'display_city', 'display_meteo')
    inlines = [MeteoInline, CityInline]
    exclude = ('meteo', 'city')


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'comment')
    prepopulated_fields = {'slug': ('name',)}


class MeteoAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'comment')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(City, CityAdmin)
admin.site.register(Meteo, MeteoAdmin)
admin.site.register(WeatherEvent, WeatherEventAdmin)

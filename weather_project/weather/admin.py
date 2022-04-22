from django.contrib import admin

from .models import Temperature, Meteo, City


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'comment', 'display_temperature', 'display_meteo')
    prepopulated_fields = {'slug': ('name',)}



class MeteoAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'comment')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(City, CityAdmin)
admin.site.register(Meteo, MeteoAdmin)

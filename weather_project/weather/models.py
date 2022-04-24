from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from pytils import translit


def slugify(s):
    new_slug = translit.slugify(s)
    return new_slug


class City(models.Model):
    """Город"""

    name = models.CharField('Название', max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    comment = models.TextField('Заметка', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('city_detail', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('city_update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('city_delete', kwargs={'slug': self.slug})

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ['name']


class Meteo(models.Model):
    """Метео"""

    name = models.CharField('Название', max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    comment = models.TextField('Заметка', blank=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Meteo, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return self.slug

    class Meta:
        verbose_name = 'Метео'
        verbose_name_plural = 'Метео'
        ordering = ['name']


class WeatherEvent(models.Model):
    """Погодное событие"""
    value = models.CharField('Значение температуры', max_length=5)
    date = models.DateField('Дата')
    time = models.TimeField('Время')
    meteo = models.ManyToManyField(Meteo, blank=True, related_name='weatherevent')
    city = models.ManyToManyField(City, blank=True, related_name='weatherevent')

    def __str__(self):
        return f'{self.value}'

    def display_meteo(self):
        return ', '.join([meteo.name for meteo in self.meteo.all()[:]])

    def display_city(self):
        return ', '.join([city.name for city in self.city.all()[:]])

    display_meteo.short_description = "Метео"
    display_city.short_description = "Город"

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'





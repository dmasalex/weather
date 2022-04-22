from django.db import models
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
    temperature = models.ManyToManyField("Temperature", blank=True, related_name='city')
    meteo = models.ManyToManyField("Meteo", blank=True, related_name='city')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(City, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

    def display_temperature(self):
        return ', '.join([temperature.name for temperature in self.temperature.all()[:]])

    def display_meteo(self):
        return ', '.join([meteo.name for meteo in self.meteo.all()[:]])

    display_temperature.short_description = "Температура"
    display_meteo.short_description = "Метео"

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


class Temperature(models.Model):
    """Температура"""

    value = models.CharField('Значение', max_length=5)
    date = models.DateTimeField('Дата/Время')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Температура'
        verbose_name_plural = 'Температура'


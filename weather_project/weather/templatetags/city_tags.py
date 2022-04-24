from django import template

from weather.models import City

register = template.Library()


@register.simple_tag()
def get_cities():
    return City.objects.all()
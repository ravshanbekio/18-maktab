from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='lowerwords')
@stringfilter
def lowerwords(value):
    return value.lower()
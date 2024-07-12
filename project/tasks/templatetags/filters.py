from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()

@register.filter(name="range")
def filter_range(start, end):
    return range(start, end)
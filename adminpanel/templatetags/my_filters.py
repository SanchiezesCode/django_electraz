from django import template
from django.utils.safestring import mark_safe
from django.db.models.fields import Field

register = template.Library()

@register.filter
def add_attrs(field, attrs):
    attributes = {}
    for attr in attrs.split(','):
        key, value = attr.split(':')
        attributes[key.strip()] = value.strip()
    
    return mark_safe(field.as_widget(attrs=attributes))



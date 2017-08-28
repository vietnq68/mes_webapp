from django import template
from django.utils.safestring import mark_safe

import json

register = template.Library()

@register.filter(name='get')
def get(d, k):
    return d.get(k, None)

@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))
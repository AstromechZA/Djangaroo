from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def fa_icon(icon_name):
    return mark_safe('<i class="fa fa-%s" aria-hidden="true"></i>' % icon_name)

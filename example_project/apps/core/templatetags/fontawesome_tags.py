from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def fa_icon(icon_name):
    """
    Example of a template tag. There are lots of other types you can register.
    They will be available for any view that does a 'load <module name>'.
    """
    return mark_safe('<i class="fa fa-%s" aria-hidden="true"></i>' % icon_name)

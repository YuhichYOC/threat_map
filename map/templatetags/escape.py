from django import template

register = template.Library()


@register.filter
def escape_backslash(value):
    return value.replace('\\', '\\\\')

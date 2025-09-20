from django import template

register = template.Library()


@register.filter
def comtodot(value):
    return value.replace(",", ".")


@register.filter
def to_str(value):
    return str(value)

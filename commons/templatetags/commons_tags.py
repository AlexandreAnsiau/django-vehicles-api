from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag(name="setting")
def get_setting(setting):
    return getattr(settings, setting)
from django import template
from django.contrib.auth.models import User

register = template.Library()

@register.filter(name='is_authenticated')
def is_authenticated(user):
    return user.is_authenticated

@register.simple_tag(name='get_user_name')
def get_user_name(user):
    if user.is_authenticated:
        return user.username
    return ''
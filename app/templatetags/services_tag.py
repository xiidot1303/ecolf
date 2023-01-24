from django import template
from app.services import language_service

register = template.Library()

@register.filter()
def string(request, text):
    text = str(text).lower()
    return language_service.get_string(text, request)

@register.filter()
def user_lang(request):
    ip = language_service.get_user_ip(request)
    return language_service.get_lang_by_ip(ip)
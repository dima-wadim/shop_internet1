from config import settings
from django import template
import os

register = template.Library()

@register.simple_tag
def mediapath(path):
    return os.path.join('/', settings.MEDIA_URL, str(path))
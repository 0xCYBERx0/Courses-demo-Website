# templatetags/course_tags.py

from django import template
from urllib.parse import urlparse

register = template.Library()

@register.filter
def get_youtube_id(url):
    """Extract YouTube Video ID from URL"""
    parsed = urlparse(url)
    if 'youtube.com' in parsed.netloc and parsed.path == '/watch':
        return parsed.query.split('v=')[1].split('&')[0]
    return url
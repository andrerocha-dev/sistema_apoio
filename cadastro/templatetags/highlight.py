import re
from django import template
from django.utils.html import escape, mark_safe

register = template.Library()


@register.filter()
def highlight(text, search):
    if not text:
        return ''
    if not search:
        return escape(text)
    try:
        esc_text = escape(text)
        esc_search = re.escape(search)
        pattern = re.compile(esc_search, re.IGNORECASE)
        highlighted = pattern.sub(
            lambda m: '<mark>{}</mark>'.format(m.group(0)), esc_text)
        return mark_safe(highlighted)
    except Exception:
        return escape(text)

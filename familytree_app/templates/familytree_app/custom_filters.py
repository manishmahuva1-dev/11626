# In your app's templatetags folder, create a new file, e.g., custom_filters.py

from django import template
from datetime import datetime

register = template.Library()

@register.filter
def age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


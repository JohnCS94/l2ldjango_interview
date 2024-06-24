from django import template
from datetime import datetime

register = template.Library()

@register.filter
def l2l_dt(value):
    if isinstance(value, str):
        try:
            date_time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
            return date_time.strftime("%Y-%m-%dT%H:%M:%S")
        except ValueError:
            return value
    
    elif isinstance(value, datetime):
        return value.strftime("%Y-%m-%dT%H:%M:%S")

    return value
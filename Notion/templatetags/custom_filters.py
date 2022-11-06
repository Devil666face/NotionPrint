from django.template import Library
from datetime import datetime
from datetime import timedelta


register = Library()

@register.simple_tag(name = 'get_categories')
def get_categories(task_list):
    if len(task_list)!=0:
        return str(task_list[0].appoint_to)
    return False

@register.simple_tag(name= 'get_dates')
def get_dates(now, period):
    now_date = datetime.strptime(now, "%Y-%m-%d")
    print('Now date: ',now_date)
    match period:
        case 'week':
            return f"?appoint_to__gte=2022-10-30&amp;appoint_to__lt=2022-11-07"
        case 'month':
            return f"?appoint_to__gte=2022-11-01&amp;appoint_to__lt=2022-12-01"
        case 'year':
            return f"?appoint_to__gte=2022-01-01&amp;appoint_to__lt=2023-01-01"
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
    def to_str(date):
        return date.strftime('%Y-%m-%d')
        
    now_date = datetime.strptime(now, "%Y-%m-%d")
    # match period:
    #     case 'week':
    #         return f"?appoint_to__gte=2022-10-30&amp;appoint_to__lt=2022-11-07"
    #     case 'month':
    #         return f"?appoint_to__gte=2022-11-01&amp;appoint_to__lt=2022-12-01"
    
    if period=='week':
        return f"?appoint_to__gte={to_str(now_date-timedelta(7))}&appoint_to__lt={to_str(now_date+timedelta(1))}"
    elif period=='month':
        return f"?appoint_to__gte={to_str(now_date-timedelta(30))}&appoint_to__lt={to_str(now_date+timedelta(1))}"
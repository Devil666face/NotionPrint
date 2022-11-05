from django.template import Library
register = Library()

@register.simple_tag(name = 'get_categories')
def get_categories(task_list):
    if len(task_list)!=0:
        return str(task_list[0].appoint_to)
    return False
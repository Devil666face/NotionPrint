
from django.urls import path
from .views import *

urlpatterns = [
    # path('task'),
    # path('type'),
    path('add-task/', CreateTask.as_view(), name='add_task'),
    path('add-type/', CreateTyping.as_view(), name='add_typing'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('login/', UserLogin.as_view(), name='login'),
    path('print/', PrintTasks.as_view(), name='print'),
    path('api/', PrintAPI.as_view(), name='api'),
    path('', Home.as_view(), name='home')
]

from datetime import datetime
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .models import Task, Typing
from .forms import TaskForm, TypingForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import ListView, DetailView, CreateView, View
from django.urls import reverse_lazy
from django.views.generic.base import RedirectView
from django.core.paginator import Paginator
from django.http import (
    HttpResponse,
)
from .serialize import UTF8JsonResponse, TaskJson


def get_now_date():
    return datetime.today().strftime('%Y-%m-%d')


def get_weekday(date):
    # match datetime.isoweekday(datetime.strptime(date, "%Y-%m-%d")):
    #     case 1: return 'Понедельник'
    #     case 2: return 'Вторник'
    #     case 3: return 'Среда'
    #     case 4: return 'Четверг'
    #     case 5: return 'Пятница'
    #     case 6: return 'Суббота'
    #     case 7: return 'Воскресенье'
    day_index = datetime.isoweekday(datetime.strptime(date, "%Y-%m-%d"))
    if day_index==1: return 'Понедельник'
    elif day_index==2: return 'Вторник'
    elif day_index==3: return 'Среда'
    elif day_index==4: return 'Четверг'
    elif day_index==5: return 'Пятница'
    elif day_index==6: return 'Суббота'
    elif day_index==7: return 'Воскресенье'


class PrintAPI(RedirectView):
    def get(self, request, *args, **kwargs) -> HttpResponse:
        self.date_for_print = request.GET.get('date')
        json = TaskJson(self.date_for_print).get_json()
        return UTF8JsonResponse(json, safe=False)

class DeactivateTask(LoginRequiredMixin, RedirectView):    
    login_url = '/login/'
    def get(self, request, *args, **kwargs) -> HttpResponse:
        self.pk = request.GET.get('pk')
        Task.objects.filter(pk=self.pk).update(active=False)
        return HttpResponse(f'Task pk={self.pk} - deactivate')
        # return redirect('home')
        # return reverse_lazy('home')
    

class PrintTasks(LoginRequiredMixin, RedirectView):
    form_class = TaskForm
    login_url = '/login/'
    def get(self, request, *args, **kwargs) -> HttpResponse:
        self.date_for_print = request.GET.get('date')
        print(self.date_for_print)
        #Создать json и отправить его TG боту через requests
        return redirect('home')
    

class Home(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'Notion/home.html'
    login_url = '/login/'
    context_object_name = 'task_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['weekday'] = get_weekday(self.current_date)
        context['now_date'] = get_now_date()
        # print(context['weekday'])
        return context


    def get(self, request, *args, **kwargs) -> HttpResponse:       
        self.current_date = request.GET.get('search', get_now_date())
        self.appoint_to__gte = request.GET.get('appoint_to__gte', None)
        self.appoint_to__lt = request.GET.get('appoint_to__lt', None)
        return super().get(request, *args, **kwargs)
    

    def get_queryset(self):
        if self.appoint_to__gte!=None and self.appoint_to__lt!=None:
            return Task.objects.filter(active=True, appoint_to__gte=self.appoint_to__gte, appoint_to__lt=self.appoint_to__lt).select_related('typing')
        return Task.objects.filter(active=True, appoint_to=self.current_date).select_related('typing')


class UserLogout(LogoutView):
    next_page = '/login/'


class UserLogin(LoginView):
    authentication_form = UserLoginForm
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = '/'


class CreateTask(LoginRequiredMixin, CreateView):
    form_class = TaskForm
    template_name = 'Notion/add_task.html'
    login_url = '/login/'
    success_url = reverse_lazy('add_task')


class CreateTyping(LoginRequiredMixin, CreateView):
    form_class = TypingForm
    template_name = 'Notion/add_typing.html'
    login_url = '/login/'
    success_url = reverse_lazy('add_typing')

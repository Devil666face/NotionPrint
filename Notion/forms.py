from django import forms
from .models import Task, Typing
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs = {
        "class":"form-control",
        "placeholder":"Имя пользователя"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs = {
        "class":"form-control",
        "placeholder":"Пароль"}))


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','content','appoint_to','photo','typing']
        # widgets = {
        #     'title':forms.TextInput(attrs={"class":"form-control"}),
        #     'content':forms.Textarea(attrs={"class":"form-control"}),
        #     # 'appoint_to':forms.DateInput(attrs={"class":"form-control"}),
        #     'appoint_to':forms.DateInput(attrs={"class":"form-control","id":"appoint_to","placeholder":"MM.DD.YYYY","type":"text"}),
        #     'photo':forms.FileInput(attrs={"class":"form-control"}),
        #     'typing':forms.Select(attrs={"class":"form-select"}),
        # }


class TypingForm(forms.ModelForm):
    class Meta:
        model = Typing
        fields = '__all__'
        # widgets = {
        #     'title':forms.TextInput(attrs={"class":"form-control"}),
        # }

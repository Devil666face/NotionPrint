import json
from dataclasses import field, fields
from textwrap import indent
from django.http.response import JsonResponse
from django.core import serializers
from .models import Task, Typing


class UTF8JsonResponse(JsonResponse):
    def __init__(self, *args, json_dumps_params=None, **kwargs):
        json_dumps_params = {"ensure_ascii": False, **(json_dumps_params or {})}
        super().__init__(*args, json_dumps_params=json_dumps_params, **kwargs)


class TaskJson:
    def __init__(self,date) -> None:
        self.current_date = date
        

    def get_json(self): 
        task = serializers.serialize('json', self.get_task_from_model(self.current_date))
        typing = serializers.serialize('json', self.get_type_from_model())
        return self.modify_json({'task':task, 'type':typing})
        

    def get_task_from_model(self, date):
        data = Task.objects.filter(active=True, appoint_to=date).select_related()
        return data


    def get_type_from_model(self):
        type = Typing.objects.all()
        return type


    def modify_json(self, data):
        task_obj = json.loads(data.get('task'))
        type_dict = {key.get('pk'):key.get('fields').get('title') for key in json.loads(data.get('type'))}
        for key in task_obj:
            type_for_task = type_dict[key.get('fields').get('typing')]
            key['fields']['typing'] = type_for_task
        return task_obj

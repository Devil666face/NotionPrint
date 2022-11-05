import requests
import config
from datetime import datetime


class Utils:
    def __init__(self) -> None:
        self.session = requests.Session()

    def get_current_date(self) -> str:
        return datetime.now().strftime("%Y-%m-%d")

    def get_current_json_task(self):
        response = self.session.get(f'{config.API}?date={self.get_current_date()}')
        doc = DocumentMaker(response.json())


class DocumentMaker:
    def __init__(self, json_data) -> None:
        self.data = json_data
        self.make_document()

    def make_document(self):
        text_list = [self.make_one_task_text(key.get('fields')) for key in self.data]
        document_text = "\n".join(text_list)
        print(document_text)

    def make_one_task_text(self, task_fields):
        text = list()
        text.append(f"{task_fields.get('title')} : {task_fields.get('appoint_to')}")
        text.append(f"{task_fields.get('typing')}")
        text.append(f"{task_fields.get('content')}")
        text.append("\n")
        return "\n".join(text)

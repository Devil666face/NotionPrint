import os
from docxtpl import DocxTemplate
from datetime import datetime

class DocUtils:
    def get_doc_name(self, date:str, data_json):
        if len(data_json)==0:
            return
        doc_name = str(DocumentMaker(data_json, date))
        return doc_name


class DocumentMaker:
    def __init__(self, json_data, date) -> None:
        self.data = json_data
        self.date = date
        self.doc_name = self.make_document()

    def get_path_to_save(self):
        path_to_save = datetime.today().strftime('media/uploads/%Y/%m/%d/')
        if not os.path.exists(path_to_save):
            os.makedirs(path_to_save)
        return path_to_save

    def make_document(self):
        text_list = [self.make_one_task_text(key.get('fields'),index+1) for index,key in enumerate(self.data)]
        document_text = "\n".join(text_list)
        # print(os.listdir())
        template = DocxTemplate('Notion/DocUtils/template.docx')       
        template.render({"data":document_text})
        doc_name = f"Задачи на {self.date}.docx"
        doc_path = f"{self.get_path_to_save()}{doc_name}"
        template.save(doc_path)
        # uploads/%Y/%m/%d/
        return doc_path
        
    def make_one_task_text(self, task_fields, index):
        text = list()
        text.append(f"{index}. {task_fields.get('title')}")
        text.append(f"{task_fields.get('appoint_to')}")
        text.append(f"{task_fields.get('typing')}")
        text.append(f"{task_fields.get('content')}")
        text.append("\n")
        return "\n".join(text)

    def __str__(self) -> str:
        return self.doc_name

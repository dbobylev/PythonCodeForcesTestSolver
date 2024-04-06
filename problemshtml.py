'''
Класс для загрузки html с задачей и тест кейсами
С возможностью сохранения html на диске, для дебага
'''
from urllib.request import Request, urlopen 

import os.path

class ProblemsHtml():
    def __init__(self, task, saveHtml = False):
        self.task = task
        self.saveHtml = saveHtml
    
    def GetHtml(self):
        if os.path.isfile(self.task.html_file_name):
            print(f'Найден сохраненный файл html: {self.task.html_file_name}')
            with open(self.task.html_file_name, encoding="utf-8") as file:
                html = file.read()
        else:
            print(f'Загружаем файл html по URL: {self.task.url_path}')
            
            req = Request(self.task.url_path)
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0')
            req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8')
            html = urlopen(req).read().decode("utf8")
            if self.saveHtml:
                with open(self.task.html_file_name, 'w', encoding="utf-8") as file:
                    file.write(html)
        print(f'Длина файла: {len(html)}')
        return html
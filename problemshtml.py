import urllib.request
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
            print(f'Загружаем файл по URL: {self.task.url_path}')
            request = urllib.request.urlopen(self.task.url_path)
            html = request.read().decode("utf8")
            request.close()
            if self.saveHtml:
                with open(self.task.html_file_name, 'w', encoding="utf-8") as file:
                    file.write(html)
        print(f'Длина файла: {len(html)}')
        return html
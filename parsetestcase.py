'''Парсер тест кейсов со страницы задачи CodeForces'''
from problemshtml import ProblemsHtml
from codeforcestask import CodeForcesTask
from bs4 import BeautifulSoup
from testcase import TestCase
import os.path
import json

class ParseTestCases():
    def __init__(self, task_num, task_char):
        self.task = CodeForcesTask(task_num, task_char)

    def __GetPreText(self, node):
        return node.findChildren("pre" , recursive=False)[0].get_text(separator="\n")

    def GetTextCases(self):
        if os.path.isfile(self.task.testcase_file_name):
            print(f'Найден файл с тест кейсами: {self.task.testcase_file_name}')
            with open(self.task.testcase_file_name) as file:
                json_data = file.read()
            result = [TestCase(**json.loads(x)) for x in json.loads(json_data)]
        else:
            site = ProblemsHtml(self.task)
            html = site.GetHtml()
            soup = BeautifulSoup(html, 'html.parser')
            div_input = soup.find_all(class_="input")
            div_output = soup.find_all(class_="output")
            result = []
            for i in range(len(div_input)):
                text_input = self.__GetPreText(div_input[i])
                text_output = self.__GetPreText(div_output[i]).replace('\n','\r\n')
                result.append(TestCase(text_input, text_output))
            jsontext = [json.dumps(x.__dict__) for x in result]
            print(f'Сохраняем файл с тест кейсами: {self.task.testcase_file_name}')
            with open(self.task.testcase_file_name, 'w') as filejson:
                json.dump(jsontext, filejson)
        '''
        for x in result:
            print('=== Тест кейс ===')
            print('Input:')
            print(x.input)
            print('Output:')
            print(x.output)
        '''
        print(f'Кол-во тест кейсов: {len(result)}')
        return result
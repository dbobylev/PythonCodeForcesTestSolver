'''Парсер тест кейсов со страницы задачи CodeForces'''
from problemshtml import ProblemsHtml
from codeforcestask import CodeForcesTask
from bs4 import BeautifulSoup
from testcase import TestCase
import os.path
import json
import hashlib
from datetime import datetime

class ProblemSet():
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
            html = ProblemsHtml(self.task).GetHtml()
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
    
    def SaveSolution(self, solution, hasError):

        IsNewSolve = True
        texthash = hashlib.sha1(solution.encode('utf-8')).hexdigest()
        
        if os.path.isfile(self.task.solve_file_name):
            with open(self.task.solve_file_name, 'r') as file:
                data = file.read()
                IsNewSolve = texthash not in data

        if IsNewSolve:
            with open(self.task.solve_file_name, 'a', encoding='utf-8') as file:
                comment = f'\n##### Решение {datetime.now()} {"FAIL" if hasError else "Done"} hash: {texthash}\n\n{solution}\n\n\n'
                file.write(comment)




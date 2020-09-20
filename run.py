''' 
Запуск тест-кейсов с CodeForces
В task_num, task_char необходимо указать номер решаемой задачи. Выполнить этот(run.py) скрипт
Тест-кейсы будут загружены с сайта CodeForces и запущенный для вашего решения в файле problem_solve.py
'''
import subprocess
from parsetestcase import ParseTestCases

task_num = 71
task_char = 'A'

class RunTests():
	def __init__(self):
		self.cmd = 'python problem_solve.py < input.txt'
		self.testcases = ParseTestCases(task_num, task_char).GetTextCases()
	
	def Run(self):
		i = 1
		for case in self.testcases:
			# Сохраняем входные данные по тест кейсу в файле input.txt
			with open('input.txt', 'w') as file:
				file.write(case.input)
			
			# Запускаем процесс выполнения нашей задачи
			process = subprocess.Popen(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
			out, err = process.communicate()
		  	
			# Критичные ошибки
			if err:
				print(f'Ошибка при выполнении теста {i}')
				print(err.decode("utf-8"))
				break

			# Достаём результат выполнения и сравниваем с результатом тест-кейса
			result = out.decode("utf-8").rstrip()
			if case.output != result:
				print(f'\nОшибка результата при выполнении теста {i}:\n{case.input}')
				print(f'\nРезультат:\n{result}')
				print(f'\nОжидалось:\n{case.output}')
			else:
				print(f'Тест {i} пройден')
			i += 1

if __name__ == "__main__":
	x = RunTests()
	x.Run()
import subprocess
from parsetestcase import ProblemSet

class RunTests():
	def __init__(self, task_num, task_char):
		self.cmd = 'python problem_solve.py runtest < input.txt'
		self.problemset = ProblemSet(task_num, task_char)
	
	def Run(self):
		i = 1
		HasError = False
		testcases = self.problemset.GetTextCases()

		for case in testcases:
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
				HasError = True
				break

			# Достаём результат выполнения и сравниваем с результатом тест-кейса
			result = out.decode("utf-8").rstrip()
			if case.output != result:
				print(f'\nОшибка результата при выполнении теста {i}:\n{case.input}')
				print(f'\nРезультат:\n{result}')
				print(f'\nОжидалось:\n{case.output}')
				HasError = True
			else:
				print(f'Тест {i} пройден')
			i += 1

		# Сохраняем вариант решения
		solve = []
		with open('problem_solve.py', 'r', encoding="utf-8") as file:
			readcodeflag = False
			for line in file:
				l = line.strip()
				if readcodeflag and len(l) > 0:
					solve.append(l)
				if '#### РЕШЕНИЕ ####' in l:
					readcodeflag = True
		
		self.problemset.SaveSolution('\n'.join(solve), HasError)

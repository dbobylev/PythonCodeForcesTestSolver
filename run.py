import subprocess
from parsetestcase import ParseTestCases

cmd = 'python problem_solve.py < input.txt'

task_num = 4
task_char = 'A'

parser = ParseTestCases(task_num, task_char)
testcases = parser.GetTextCases()
i = 1
for case in testcases:
	with open('input.txt', 'w') as file:
		file.write(case.input)
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
	out, err = p.communicate()
	result = out.decode("utf-8").rstrip()
	if case.output != result:
		print(f'Ошибка при выполнении теста {i}:\n{case.input}')
		print(f'Результат:\n{result}')
		print(f'Ожидалось:\n{case.output}')
	else:
		print(f'Тест {i} пройден')
	i += 1
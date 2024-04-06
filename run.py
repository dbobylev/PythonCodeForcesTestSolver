''' 
Запуск тест-кейсов с CodeForces
В task_num, task_char необходимо указать номер решаемой задачи. Выполнить этот(run.py) скрипт
Тест-кейсы будут загружены с сайта CodeForces и запущенный для вашего решения в файле problem_solve.py

ручной запуск
'''
from runtests import RunTests

task_num = 71
task_char = 'A'

x = RunTests(task_num, task_char)
x.Run()
############## АВТОМАТИЧЕСКИЙ ЗАПУСК ТЕСТОВ ##############

import sys
from runtests import RunTests
if len(sys.argv) < 2 or sys.argv[1] != 'runtest':
    RunTests(282, 'A').Run()
    sys.exit(0)

###################### РЕШЕНИЕ ###########################

print(sum([int(x[1]+'1') for x in [*open(0)][1:]]))
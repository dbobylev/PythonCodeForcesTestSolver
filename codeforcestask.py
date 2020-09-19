import os.path

class CodeForcesTask():
    def __init__(self, task_num, task_char):
        self.task_num = task_num
        self.task_char = task_char
        self.str_task_num = str(task_num).rjust(4, '0')
        self.html_directory_name = 'problemset_html'
        self.html_file_name = f'{self.html_directory_name}/{self.str_task_num}_{task_char}.html'
        self.testcase_directory_name = 'problemset'
        self.testcase_file_name = f'{self.testcase_directory_name}/{self.str_task_num}_{task_char}.json'
        self.url_path = f'https://codeforces.com/problemset/problem/{task_num}/{task_char}'
        if not os.path.exists(self.html_directory_name):
            os.makedirs(self.html_directory_name)
        if not os.path.exists(self.testcase_directory_name):
            os.makedirs(self.testcase_directory_name)
''' Отдельный тест кейс '''
import json

class TestCase():
    def __init__(self, input, output):
        self.input = input
        self.output = output
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
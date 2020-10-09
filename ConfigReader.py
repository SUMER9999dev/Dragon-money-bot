import json


class Reader(object):
    def __init__(self):
        with open('config.json', 'r') as reader:
            self.json_object = json.loads(reader.read())
        
    def auto_conclusion(self):
        return self.json_object['auto_conclusion']
        
    def balance_divide_value(self):
        return self.json_object['balance_divide_value']
    
    def tactic(self):
        return self.json_object['tactic']

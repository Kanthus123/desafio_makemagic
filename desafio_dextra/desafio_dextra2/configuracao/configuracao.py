import json
from os_path import configuracao_path

class Config:
    def __init__(self):
        with open(configuracao_path()) as json_data_file:
            self.data = json.load(json_data_file)

    def secret_key(self):
        return self.data["secret"]


import json

class Makanan:
    data = {}
    cfg_path = ""
    def __init__(self,path):
        self.cfg_path = path
        c = open(self.cfg_path,"r")
        self.data = json.loads(c.read())

    def getData(self):
        return self.data
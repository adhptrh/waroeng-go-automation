import json

class Config:
    data = {}
    cfg_path = ""
    cfg_names = {
        "auth":"authorization",
        "channel_id":"channel_id"
    }

    def __init__(self,config_path):
        self.cfg_path = config_path
        c = open(self.cfg_path,"r")
        self.data = json.loads(c.read())

    def getAuthorization(self):
        return self.data[self.cfg_names["auth"]]

    def setAuthorization(self,new_auth):
        self.data[self.cfg_names["auth"]] = new_auth

    def getChannelId(self):
        return self.data[self.cfg_names["channel_id"]]

    def setChannelId(self, new_channel_id):
        self.data[self.cfg_names["channel_id"]] = new_channel_id

    def save(self):
        s = open(self.cfg_path,"w")
        s.write(json.dumps(self.data))

    def reset(self):
        self.data = {
            self.cfg_names["auth"]:"",
            self.cfg_names["channel_id"]:""
        }

        self.save()
import json,requests,re

class Bot:
    data = {}
    cfg_path = ""
    cfg_names = {
        "auth":"authorization",
        "channel_id":"channel_id"
    }

    api_link = "https://discord.com/api/v9"

    def __init__(self,config_path):
        self.cfg_path = config_path

        try:
            c = open(self.cfg_path,"r")
            self.data = json.loads(c.read())

        except FileNotFoundError:
            c = open(self.cfg_path,"w")
            self.data = self.blankData()
            c.write(json.dumps(self.data))

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

    def blankData(self):
        return {
            self.cfg_names["auth"]:"",
            self.cfg_names["channel_id"]:""
        }

    def reset(self):
        self.data = self.blankData()

        self.save()

    def generateHeader(self):
        return {
            "authorization":self.data[self.getAuthorization()]
        }

    def getLastChannelMessage(self):
        r = requests.get(f"{self.api_link}/channels/{self.getChannelId()}/messages?limit=1",headers=self.generateHeader())
        return r.json()

    def sendMessage(self,message):
        pdata = {
            "content":message
        }
        r = requests.post(f"{self.api_link}/channels/{self.getChannelId()}/messages",headers=self.generateHeader(),json=pdata)
        return r.json()
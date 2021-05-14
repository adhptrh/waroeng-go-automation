import json,requests,re

class Bot:
    data = {}
    cfg_path = ""
    cfg_names = {
        "auth":"authorization",
        "channel_id":"channel_id"
    }

    discord = ""

    def __init__(self,config_path):
        self.cfg_path = config_path

        try:
            c = open(self.cfg_path,"r")
            self.data = json.loads(c.read())

        except FileNotFoundError:
            c = open(self.cfg_path,"w")
            self.data = self.blankData()
            c.write(json.dumps(self.data))
        
        self.reauthDiscord()

    def getAuthorization(self):
        return self.data[self.cfg_names["auth"]]

    def setAuthorization(self,new_auth):
        self.data[self.cfg_names["auth"]] = new_auth
        self.reauthDiscord()

    def getChannelId(self):
        return self.data[self.cfg_names["channel_id"]]

    def setChannelId(self, new_channel_id):
        self.data[self.cfg_names["channel_id"]] = new_channel_id
        self.reauthDiscord()

    def save(self):
        s = open(self.cfg_path,"w")
        s.write(json.dumps(self.data))

    def reauthDiscord(self):
        self.discord = Bot.Discord(self.getAuthorization(),self.getChannelId())

    def blankData(self):
        return {
            self.cfg_names["auth"]:"",
            self.cfg_names["channel_id"]:""
        }

    def reset(self):
        self.data = self.blankData()
        self.save()

    class Discord:
        api_link = "https://discord.com/api/v9"
        authorization = ""
        channel_id = ""

        def generateHeader(self):
            return {
                "authorization":self.authorization
            }
        
        def __init__(self,authorization,channel_id):
            self.authorization = authorization
            self.channel_id = channel_id

        def getLastChannelMessage(self):
            r = requests.get(f"{self.api_link}/channels/{self.channel_id}/messages?limit=1",headers=self.generateHeader())
            return r.json()

        def sendMessage(self,message):
            pdata = {
                "content":message
            }
            r = requests.post(f"{self.api_link}/channels/{self.channel_id}/messages",headers=self.generateHeader(),json=pdata)
            return r.json()
import requests, time, json, re
from bot.bot import Bot
config = Bot("config.json")

print("""
Waroeng-Go Automation Bot
[=---------------------------=]
""")

if not config.getAuthorization():
    config.setAuthorization(input("Put your discord authorization here : "))

if not config.getChannelId():
    config.setChannelId(input("Put your server channel id : "))

config.save()
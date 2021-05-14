import requests, time, json, re
from bot.bot import Bot
bot = Bot("config.json")

print("""
Waroeng-Go Automation Bot
[=---------------------------=]
""")

if not bot.getAuthorization():
    bot.setAuthorization(input("Put your discord authorization here : "))

if not bot.getChannelId():
    bot.setChannelId(input("Put your server channel id : "))

bot.save()
print(bot.discord.sendMessage("test 2"))
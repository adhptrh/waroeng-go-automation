import requests, time, json, re, colorama
from bot.bot import Bot
from makanan.makanan import Makanan
from colorama import Fore
colorama.init(autoreset=True)

bot = Bot("config.json")
makanan = Makanan("makanan.json")

print(f"""{Fore.LIGHTBLUE_EX}
[=---------------------------=]
|  Waroeng-Go Automation Bot  |
[=---------------------------=]
""")

if not bot.getAuthorization():
    bot.setAuthorization(input("Put your discord authorization here : "))

if not bot.getChannelId():
    bot.setChannelId(input("Put your server channel id : "))

bot.save()

print(f"""{Fore.LIGHTWHITE_EX}1. Tambah Makanan
2. Hapus Makanan
3. List Makanan
4. Start Bot
""")

choice = int(input(f"[1,2,3,4] : "))

print("")
if choice == 3:
    mkns = makanan.getData()
    for k,v in mkns.items():
        print(f"{Fore.LIGHTGREEN_EX}- {k.title()}")
        print(f"{Fore.YELLOW}  Bahan : ")
        for kk,vv in v["bahan"].items():
            print(f"     - {kk.title()} : Rp. {vv}")

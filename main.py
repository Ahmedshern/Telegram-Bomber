# Telegram Bomber - DociTeam
# YouTube Video : https://youtu.be/pWHHpnPz0jc

from sched import scheduler
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
import os
import time
from datetime import timedelta


def clear_console():
    if os.name in ("nt", "dos"):  # Check OS name for using correct command
        try:
            os.system("cls")
        except:
            pass
    else:
        try:
            os.system("clear")
        except:
            pass


def change_title():
    if os.name in ("nt", "dos"):
        try:
            os.system('title "DociTeam | Telegram Bomber"')
        except:
            pass
    else:
        pass


clear_console()
change_title()


class color:
    Red = "\033[91m"
    Green = "\033[92m"
    Blue = "\033[94m"
    Cyan = "\033[96m"
    White = "\033[97m"
    Yellow = "\033[93m"
    Magenta = "\033[95m"
    Grey = "\033[90m"
    Black = "\033[90m"
    Default = "\033[99m"


dociteam = (
    color.Cyan
    + """
                                     ____             _ _____                    
                                    |  _ \  ___   ___(_)_   _|__  __ _ _ __ ___  
                                    | | | |/ _ \ / __| | | |/ _ \/ _` | '_ ` _ \ 
                                    | |_| | (_) | (__| | | |  __/ (_| | | | | | |
                                    |____/ \___/ \___|_| |_|\___|\__,_|_| |_| |_|
"""
)


API_ID = int(19885263)
API_HASH = str("9e7886b2a397aa73b0eab3e2532fef0c")
PHONE = str("+9607248949")
TARGET = str("https://t.me/GoldenFrogInu1000x")  # ID Ex : @dociteam
MESSAGE = str("/FROG_INU_60X_GOLDEN_FROG_600X")
COUNTER = int(1000)


client = TelegramClient("session", API_ID, API_HASH)
client.start()
print(color.Green + "[+] Lets Start...\n")


async def main():
    if not await client.is_user_authorized():
        await client.send_code_request(PHONE)
        try:
            await client.sign_in(PHONE, input(color.Yellow + "[+] Enter the code : "))
        except SessionPasswordNeededError:
            await client.sign_in(password=input(color.Yellow + "[+] Password : "))
    for i in range(1, int(COUNTER) + 1):
        time.sleep(10)
        await client.send_message(
            TARGET,
            MESSAGE,
        )
        print(color.Green + "[+] Message Has Sent!\n")
    input(color.Green + "\nPress Enter To Quit........")


with client:
    client.loop.run_until_complete(main())

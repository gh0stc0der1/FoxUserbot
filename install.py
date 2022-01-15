import os
from colorama import Fore
import time
from plugins.help import requirements_list

for rq in requirements_list:
    os.system(f"pip install {rq}")
    
os.system("clear")

print(Fore.GREEN + "Привет. Добро пожаловать в установщик FoxUserBot.")
time.sleep(1)
print(Fore.GREEN + "Введите ваш api id. Его можно найти на сайте my.telegram.org")
api_id = input(Fore.GREEN + ">>> ")
print(Fore.GREEN + "Спасибо. Введите api hash.")
api_hash = input(Fore.GREEN + ">>> ")
config = open('config.ini', '+w')
config.write(f"""[pyrogram]
api_id = {api_id}
api_hash = {api_hash}""")
config.close()
print(Fore.GREEN + "Спасибо. Данные сохранены. Сейчас вам предложат ввести номер и код из смс, сделайте это для установки FoxUserBot.")
os.system("python3 main.py")
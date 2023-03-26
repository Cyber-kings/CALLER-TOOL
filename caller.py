import os
import time
import colorama
from colorama import Fore,Back,Style

colorama.init(autoreset=True)

print(Fore.RED+Style.BRIGHT+'''
   _____          _      _      ______ _____     _______ ____   ____  _
  / ____|   /\   | |    | |    |  ____|  __ \   |__   __/ __ \ / __ \| |
 | |       /  \  | |    | |    | |__  | |__) |_____| | | |  | | |  | | |
 | |      / /\ \ | |    | |    |  __| |  _  /______| | | |  | | |  | | |
 | |____ / ____ \| |____| |____| |____| | \ \      | | | |__| | |__| | |____
  \_____/_/    \_\______|______|______|_|  \_\     |_|  \____/ \____/|______|CY KING''')

print ()

print(Fore.RED+Style.BRIGHT+'Loading....')
time.sleep(5)
os.system('apt update && apt upgrade -y')
print(Fore.YELLOW+Style.BRIGHT+'IF THIS TOOL MACK AN ERROR INSTALL TERMUX API FROM PLAYSTORE')
print(Fore.YELLOW+Style.BRIGHT+'Read the message')
time.sleep(7)
os.system('apt install termux-api')
X = input(Style.BRIGHT+Fore.RED+'Enter Number:-')

os.system('termux-telephony-call ' + X)
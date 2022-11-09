
from termcolor import colored
from operator import imod
import os
import caeser
import vigener
import Hill
import Autokey
import playfiar
import AES
import RSA
import RailFence
import pyfiglet
import offine
import multiplicative
app_name=colored(pyfiglet.figlet_format("EncipherSec"),'green')



print(app_name)

print("please choose the algorithm that you want :")
print("1- Auto-Key")
print("2- Casear")
print("3- Playfire")
ch=input()
match ch :
    case "1":os.system('cls' if os.name == 'nt' else 'clear') ; Autokey.display_Auto()
    case "2":os.system('cls' if os.name == 'nt' else 'clear') ; caeser.display_caeser()
    case "3":os.system('cls' if os.name == 'nt' else 'clear') ; playfiar.display_Play()
    case "4":os.system('cls' if os.name == 'nt' else 'clear') ; vigener.display_vig()
    case "5":os.system('cls' if os.name == 'nt' else 'clear') ; Hill.display_hill()
    case "6":os.system('cls' if os.name == 'nt' else 'clear') ; AES.display_Aes()
    case "7":os.system('cls' if os.name == 'nt' else 'clear') ; RSA.display_RSA()
    case "8":os.system('cls' if os.name == 'nt' else 'clear') ; RailFence.display_railfence()
    case "9":os.system('cls' if os.name == 'nt' else 'clear') ; offine.display_()
    case "10":os.system('cls' if os.name == 'nt' else 'clear') ; multiplicative.display_multi()



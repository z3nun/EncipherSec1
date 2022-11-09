from pydoc import plain
from re import I
from termcolor import colored
import pyfiglet
crp_alg="Multiplicative"
app_name=colored(pyfiglet.figlet_format("CrypZ3nun - "+crp_alg),'green')

alphabet= "abcdefghijklmnopqrstuvwxyz"
index = dict(zip(alphabet,range(len(alphabet))))
letter = dict(zip(range(len(alphabet)),alphabet))

def encryptmulti(message,key):
   plain=message
   cipher=''
   for char in plain:
       if char=='':
          cipher=cipher+char
       elif char.isupper():
            cipher=cipher + chr((ord(char) * int(key) -65)%26 + 65)
       else:
            cipher=cipher + chr((ord(char) * int(key) -97)%26 + 97)
   return cipher


def decryptmulti(message):
   plain=message
   invkey=[1,9,21,15,3,19,7,23,11,5,17,25]
   
   for i in range(12):
    cipher=''   
    for char in plain:
       if char=='':
          cipher=cipher+char
       elif char.isupper():
            cipher=cipher + chr((ord(char) * int(invkey[i]) -65)%26 + 65)
       else:
            cipher=cipher + chr((ord(char) * int(invkey[i]) -97)%26 + 97)
    print('\n hacking invkey #%s: %s'%(invkey[i],cipher))
          
   
      
   
        


def display_multi():  
   print(app_name)
   print("please choose :")
   print("1-encrypt...")
   print("2-decrypt...")
   choosed = input()
   match choosed:
       case "1": print("please enter your message ") ; message=input(); print("please enter the key") ; key=input(); cipher=encrypt(message,key); print("CIPHER is :" +cipher)
       case "2": print("please enter your encrypted message :"); message=input(); plain=decrypt(message); print(plain)
from termcolor import colored
import pyfiglet
crp_alg="Caeser"
app_name=colored(pyfiglet.figlet_format("CrypZ3nun - "+crp_alg),'green')



alphabet= "abcdefghijklmnopqrstuvwxyz"
index = dict(zip(alphabet,range(len(alphabet))))
letter = dict(zip(range(len(alphabet)),alphabet))

def encrypt(message,key):
   cipher=''
   for i in range(0,len(message)):
      cipher = cipher + letter[((index[message[i]] +index[key]) % 26)]
   return cipher

def decrypt(message):
   
   for j in range(0,len(alphabet)):
      plain=''
      for i in range(len(message)):
         plain= plain + letter[((index[message[i]] - index[letter[j]]) %26)]
         k="key "
      print ("{}{}" .format( k , index[letter[j]]))
      print("    : "+ plain)
def display_caeser():  
   print(app_name)
   print("please choose :")
   print("1-encrypt...")
   print("2-decrypt...")
   choosed = input()
   match choosed:
       case "1": print("please enter your message ") ; message=input(); print("please enter the key") ; key=input(); cipher=encrypt(message,key); print("CIPHER is :" +cipher)
       case "2": print("please enter your encrypted message :"); message=input(); plain=decrypt(message); print(plain)
def display():
   cipher=encrypt(encryptmulti(input("enter your text"),input("input the multi key")),input("enter the add key"))



   plain=decrypt(decryptmulti(input))
   print(plain)
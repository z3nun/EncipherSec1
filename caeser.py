from termcolor import colored
import pyfiglet
crp_alg="Caeser"
app_name=colored(pyfiglet.figlet_format("EncipherSec - "+crp_alg),'green')



alphabet= "abcdefghijklmnopqrstuvwxyz"
index = dict(zip(alphabet,range(len(alphabet))))
letter = dict(zip(range(len(alphabet)),alphabet))

def encrypt(message,key):
   cipher=''
   for i in range(0,len(message)):
      cipher = cipher + letter[((index[message[i]] +index[key[0]]) % 26)]
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

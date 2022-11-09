from termcolor import colored
import pyfiglet
crp_alg="autoKey"
app_name=colored(pyfiglet.figlet_format("EncipherSec - "+crp_alg),'green')

alphabet= "abcdefghijklmnopqrstuvwxyz"
index = dict(zip(alphabet,range(len(alphabet))))
letter = dict(zip(range(len(alphabet)),alphabet))




def encrypt(message,key):
 cipher = ''
 cipher = cipher + letter[((index[message[0]] +int(index[key[0]])) % 26)]
 for i in range(1,len(message)):
   cipher = cipher +letter[((index[message[i]]+int(index[message[i-1]]))%26)]
 return cipher 

    


def decrypt(message,key):
    plain = ''
    plain = plain + letter[((index[message[0]] - index[key[0]])%26)]
    for i in range(1,len(message)):
        plain= plain +letter[((index[message[i]]-index[plain[i-1]])%26)]
    return plain
    print("your plain text is : (" + plain + ")")



def display_Auto():
  print(app_name)
  print("please choose :")
  print("1-encrypt...")
  print("2-decrypt...")
  choosed = input()
  match choosed :
        case "1" : print("please input your message : "); message= input(); print("please input the key"); key= input() ; cipher=encrypt(message,key); print(cipher)
        case "2" : print("please input your message : "); message= input(); print("please input the key"); key= input() ; plain=decrypt(message, key); print(plain)
    

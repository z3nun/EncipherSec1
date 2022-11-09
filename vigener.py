from termcolor import colored
import pyfiglet
crp_alg="Vigener"
app_name=colored(pyfiglet.figlet_format("EncipherSec - "+crp_alg),'green')


from itertools import starmap, cycle

def encrypt(message, key):

    # convert to uppercase.
    # strip out non-alpha characters.
    message = filter(lambda _: _.isalpha(), message.upper())

    # single letter encrpytion.
    def enc(c,k): return chr(((ord(k) + ord(c)) % 26) + ord('A'))

    return "".join(starmap(enc, zip(message, cycle(key))))

def decrypt(message, key):

    # single letter decryption.
    def dec(c,k): return chr(((ord(c) - ord(k)) % 26) + ord('A'))

    return "".join(starmap(dec, zip(message, cycle(key))))


def display_vig():
  print(app_name)
  print("please choose :")
  print("1-encrypt...")
  print("2-decrypt...")
  choosed = input()
  match choosed :
        case "1" : print("please input your message : "); message= input(); print("please input the key"); key= input() ; cipher=encrypt(message,key); print(cipher)
        case "2" : print("please input your message : "); message= input(); print("please input the key"); key= input() ; plain=decrypt(message, key); print(plain)
    

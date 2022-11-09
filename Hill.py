from email import message
from termcolor import colored
import pyfiglet
crp_alg="Hill"
app_name=colored(pyfiglet.figlet_format("EncipherSec - "+crp_alg),'green')
import numpy as np
from egcd import egcd



alphabet= "abcdefghijklmnopqrstuvwxyz"
index = dict(zip(alphabet,range(len(alphabet))))
letters = dict(zip(range(len(alphabet)),alphabet))


def matrix_mod_inv(matrix,modulus):
    det= int(np.round(np.linalg.det(matrix)))
    det_inv= egcd(det, modulus)[1]%modulus
    matrix_modulus_inv = det_inv *np.round(det*np.linalg.inv(matrix)).astype(int)%modulus
    return matrix_modulus_inv

def encrypt(message,k):
    key=np.array([k,k],[k,k])
    encrypt_message=''
    message_in_numbers=[]
    for letter in message:
        message_in_numbers.append(index[letter])

    split_p = [message_in_numbers[i:i+int(k.shape[0])] for i in range(0,len(message_in_numbers),int(k.shape[0]))]

    for p in split_p:
        p=np.transpose(np.asarray(p))
        while p.shape[0] != k.shape[0]:
            p=np.append(p,index['x'])[:,np.newaxis]

        numbers =np.dot(k,p)%len(alphabet)

        n= numbers.shape[0]
        for idx in range(n):
            number= int(numbers[idx,0])
            encrypt_message+=letters[number]
    return encrypt_message

def decrypt(cipher,kinv):
    decrypt_msg=''
    cipher_in_numbers=[]
    for letter in cipher:
        cipher_in_numbers.append(index[letter])
    
    split_c=[cipher_in_numbers[i:i+int(kinv.shape[0])] for i in range(0,len(cipher_in_numbers), int(kinv.shape[0]))]
    for c in split_c:
        c = np.transpose(np.asarray(c))[:,np.newaxis]
        numbers= np.dot(kinv,c)% len(alphabet)
        n= numbers.shape[0]
        for idx in range(n):
            number =  int(numbers[idx,0])
            decrypted+= letters[number]

    return decrypt




    
def display_hill():
   print(app_name)
   print("please choose :")
   print("1-encrypt...")
   print("2-decrypt...")
   choosed = input()
   match choosed:
       case "1": print("please enter your message ") ; message=input(); print("please enter the key") ; k=[[input(),input()],[input(),input()]]; cipher=encrypt(message,k); print("CIPHER is :" +cipher)
       case "2": print("please enter your encrypted message :"); message=input(); plain=decrypt(message); print(plain)


import random
from termcolor import colored
import pyfiglet
crp_alg="RSA"
app_name=colored(pyfiglet.figlet_format("EncipherSec - "+crp_alg),'green')


def get_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def get_encryption_key(n, phi_of_n):
    flag = 0
    while (flag == 0):
        r= random.randint(2, phi_of_n)
        gcd = get_gcd(r, n)
        gcd_phi = get_gcd(r, phi_of_n)
        if (gcd == 1) and (gcd_phi == 1):
            e=r
            flag = 1
    return e

def get_decryption_key(e , phi_of_n):
    flag = 0
    while (flag == 0 ):
        r = random.randint(2, phi_of_n)
        t = r * e
        if ( t % phi_of_n == 1) and ( r != e):
            d = r
            flag = 1
    return d
    
def encrypt(me,e,n):
    en = (me ** e)
    c = en % n
    return c
def decrypt(me,d,n):
    en = (me ** d)
    p = en % n
    return p


def RSA_E_D(p,q,string):
    n = p*q
    phi_of_n = (p-1)*(q-1)
    e= (get_encryption_key(n, phi_of_n))
    print("The Encryption_key is: e = ", e)
    d = (get_decryption_key(e, phi_of_n))
    print("The Decryption_key is: d = ", d)
    cipher = ""
    for i in string:
        s = ord(i)
        # print(s)
        c = encrypt(s,e,n)
        cipher = cipher + chr(c)
    print("The Cipher Message is: ", cipher)
    plain = ""
    for i in cipher:
        s = ord(i)
        # print(s)
        c = decrypt(s,d,n)
        plain = plain + chr(c)
    print("The plain Message is: ", plain)

def plain(cipher,key,n):
    plain = ""
    for i in cipher:
        s = ord(i)
        # print(s)
        c = decrypt(s,int(key),n)
        plain = plain + chr(c)
    print("The plain Message is: ", plain)




def display_RSA():
    print(app_name)
    print("please choose :")
    choice = input("1_encrypt   2_decrypt")
    p = 11; q = 41
    n = p*q
    if(choice=='1'):
        phi_of_n = (p-1)*(q-1)
        s=input("Enter Your Message: ")
        RSA_E_D(p,q,s)
    elif(choice=='2'):
        message=input("Enter the cipher: ")
        key=input("Enter the key: ")
        plain(message,key,n)
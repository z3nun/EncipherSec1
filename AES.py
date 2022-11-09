from Crypto.Cipher import AES
from secrets import token_bytes
key=token_bytes(16)

def encrypt(txt,key):
    cipher=AES.new(key,AES.MODE_EAX)
    nonce=cipher.nonce
    cipherText , tag =cipher.encrypt_and_digest(txt)
    return nonce , cipherText, tag

def decrypt(nonce, cipherText, tag):
    cipher=AES.new(key)
    plainText=cipher.decrypt(cipherText)
    try:
        cipher.verify(tag)
        return plainText,tag
    except:
        return False

def display_Aes():
 
   print("please choose :")
   print("1-encrypt...")
   print("2-decrypt...")
   choosed = input()
   match choosed:
       case "1": nonce,cipherText, tag=encrypt(input("Enter your message please : "),key); print("CIPHER is :" +cipherText)
       case "2": print("please enter your encrypted message :"); message=input(); plain=decrypt(message); print(plain)
 


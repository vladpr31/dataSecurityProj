from cryptography.fernet import Fernet

def generate_key():

    key = Fernet.generate_key() ##generates Key for Encryption
    with open("secret.key", "wb") as key_file: ##saves key inside secret.key
        key_file.write(key) ##write key into file.

def load_key(): ##loads the key
    return open("secret.key", "rb").read()

def encrypt_message(message):
    generate_key() ##creates the key file
    key = load_key() ##reads the key
    print("The Secret Message We Encrypt: ",message) ##inserted msg before encryption
    encoded_message = message.encode() ##encrypting the key
    f = Fernet(key) ##makes msg cannot be read without the key Fernet is an implemented function of the library.
    encrypted_message = f.encrypt(encoded_message) ##the new encrypted msg after using the key.
    with open('secretMsg.txt','wb') as secret_msg: ##saves msg inside a txt file, msg is of type byte.
        secret_msg.write(encrypted_message)
    return encrypted_message

def decrypt_message(msg):
    key = load_key() ##loads key from key file.
    f = Fernet(key) ##save the read key
    msgsv=open('secretMsg.txt','rb').read() ##opens the saved encrypted msg from txt.
    if(msg==msgsv.decode('utf-8')): ##checks if msg equals the msg we want to decode with typecasting it to utf-8
        decrypted_message = f.decrypt(msgsv) ##if the 'if' checks out then the msg is right and we decrypt it
        return decrypted_message.decode() ## return the decrypted msg
    else:
        print("Couldn't Find Your Secret, Maybe There Is None?") ##if check fails means the msg couldnt get decrypted.
        ##this can happen for 2 reasons: the msg was lost when we change the picutre foramt and some pixels went lost.
        ## or because there wasnt a msg or not enough space (pixel wise) in the image because of the sime of the msg.



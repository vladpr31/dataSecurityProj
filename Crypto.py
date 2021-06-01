from cryptography.fernet import Fernet

def generate_key():

    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message):
    generate_key()
    key = load_key()
    print("The Secret Message We Encrypt: ",message)
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    with open('secretMsg.txt','wb') as secret_msg:
        secret_msg.write(encrypted_message)
    return encrypted_message

def decrypt_message(msg):
    key = load_key()
    f = Fernet(key)
    msgsv=open('secretMsg.txt','rb').read()
    if(msg==msgsv.decode('utf-8')):
        decrypted_message = f.decrypt(msgsv)
        return decrypted_message.decode()
    else:
        print("Couldn't Find Your Secret, Maybe There Is None?")


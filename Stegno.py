1import cv2
import numpy as np
import Crypto

def to_bin(data):
    if isinstance(data, str):
        return ''.join([ format(ord(i), "08b") for i in data ])
    elif isinstance(data, bytes) or isinstance(data, np.ndarray):
        return [ format(i, "08b") for i in data ]
    elif isinstance(data, int) or isinstance(data, np.uint8):
        return format(data, "08b")
    else:
        raise TypeError("Type not supported.")

def encode(image_name, secret_data):
    image = cv2.imread(image_name)
    n_bytes = image.shape[0] * image.shape[1] * 3 // 8
    print("[*] Maximum bytes to encode:", n_bytes,"(<-This is the Size of pixels needed to embed the Data.)")
    if len(secret_data) > n_bytes:
        raise ValueError("[!] Insufficient bytes, need bigger image or less data.")
    print("[*] Hiding Super Secret Message... -->",secret_data)
    secret_data += "+++++"
    data_index = 0
    binary_secret_data = to_bin(secret_data)
    data_len = len(binary_secret_data)
    for row in image:
        for pixel in row:
            r, g, b = to_bin(pixel)
            if data_index < data_len:
                pixel[0] = int(r[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                pixel[1] = int(g[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index < data_len:
                pixel[2] = int(b[:-1] + binary_secret_data[data_index], 2)
                data_index += 1
            if data_index >= data_len:
                break
    print("[*]Secret Message Hidden![*]\n\n")
    return image

def decode(image_name):
    print("[+] Searching For Super Sneaky Secrets...")
    image = cv2.imread(image_name)
    binary_data = ""
    for row in image:
        for pixel in row:
            r, g, b = to_bin(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
    all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "+++++":
            break
    return Crypto.decrypt_message(decoded_data[:-5])

def StegnoCryp():
    print("1 - Hide Your Secret.")
    print("2 - Reveal Hidden Secret.")
    func=input()
    if func=='1':
        input_image = input("Image Name with extension (Example-> Test.png):")
        output_image = input("Image name on save with extension (Example-> StegnoTest.png):")
        secret_data = input("Enter Your Secret Message: ")
        secret_data=Crypto.encrypt_message(secret_data)
        encoded_image = encode(image_name=input_image, secret_data=secret_data.decode('utf-8'))
        cv2.imwrite(output_image, encoded_image)
    if func=='2':
        output_image = input("Image name you've saved as Stegno Image with Extension (Example -> StegnoTest.png):")
        decoded_data = decode(output_image)
        print("[+] Found Secret Message, You Tried To Hide This?->", decoded_data)
    else:
        StegnoCryp()

StegnoCryp()
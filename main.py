from generation import generation_key, encryption_key, decryption_key
from encrypt_and_decryp import encryption, decryption
import os
import json
if __name__ == '__main__':
    setting = {
        'initial_file': 'text.txt',
        'encrypted_file': 'encrypted.txt',
        'decrypted_file': 'decrypted.txt',
        'symmetric_key': 'symmetric_key.txt',
        'public_key': 'public_key.pem',
        'private_key': 'private_key.pem',

    }
    with open('settings.json', 'w') as fp:
        json.dump(setting, fp)
    with open('settings.json') as json_file:
        json_data = json.load(json_file)
    iv = os.urandom(16)
    while True:
        print("1. Generate keys")
        print("2. Encrypt text")
        print("3. Decrypt text")
        print("0. Exit the program")
        cmd = input("Chose action: ")
        if cmd == "1":
            while True:
                print("1. 128 bit")
                print("2. 192 bit")
                print("3. 256 bit")
                print("0. Exit the program")
                cmd_2 = input("Select the key length: ")
                if cmd_2 == "1":
                    generation_key(setting, 16)
                    encryption_key(setting)
                    break
                elif cmd_2 == "2":
                    generation_key(setting, 24)
                    encryption_key(setting)
                    break
                elif cmd_2 == "3":
                    generation_key(setting, 24)
                    encryption_key(setting)
                    break
                elif cmd_2 == "0":
                    break

        elif cmd == "2":
            encryption(setting, iv)

        elif cmd == "3":
            decryption(setting, iv)
        elif cmd == "0":
            break
        else:
            print("Incorrect value, enter value again")

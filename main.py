from generation import generation_key,encryption_key,decryption_key
from encrypt_and_decryp import encryption
import os
if __name__=='__main__':
    setting={
        'initial_file': 'text.txt',
        'encrypted_file': 'encrypted.txt',
        'symmetric_key':'symmetric_key.txt',
        'public_key':'public_key.pem',
        'private_key':'private_key.pem',

    }
    generation_key(setting,16)
    encryption_key(setting)
    with open(setting['symmetric_key'], mode='rb') as key_file:
        key = key_file.read()
    ds_key = decryption_key(setting, key)
    print(ds_key)
    iv=os.urandom(8)
    encryption(setting,iv)



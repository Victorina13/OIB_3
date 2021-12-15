from generation import decryption_key
from cryptography.hazmat.primitives import padding as pd
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def encryption(setting, iv):
    with open(setting['symmetric_key'], mode='rb') as key_file:
        key = key_file.read()
    ds_key = decryption_key(setting, key)
    with open(setting['initial_file'], 'r', encoding='UTF-8') as f:
        res = f.read()
        print("Start text")
        print(res)
    pad = pd.ANSIX923(128).padder()
    text = bytes(res, 'UTF-8')
    padded_text = pad.update(text) + pad.finalize()
    cipher = Cipher(algorithms.Camellia(ds_key), modes.CBC(iv))
    encryptr = cipher.encryptor()
    encryp_text = encryptr.update(padded_text) + encryptr.finalize()
    print(encryp_text)
    with open(setting['encrypted_file'], 'wb') as encryp_file:
        encryp_file.write(encryp_text)


def decryption(setting: dict, iv: bytes):

    with open(setting['symmetric_key'], mode='rb') as key_file:
        key = key_file.read()
    ds_key = decryption_key(setting, key)
    with open(setting['encrypted_file'], mode='rb') as dc_file:
        enc_text = dc_file.read()
    cipher = Cipher(algorithms.Camellia(ds_key), modes.CBC(iv))
    decrypter = cipher.decryptor()
    dc_text = decrypter.update(enc_text) + decrypter.finalize()
    unpad = pd.ANSIX923(128).unpadder()
    unpadded_dc_text = unpad.update(dc_text) + unpad.finalize()
    res = unpadded_dc_text.decode('UTF-8')
    print("Decryption text")
    print(res)
    with open(setting['decrypted_file'], 'w') as dec_file:
        dec_file.write(res)
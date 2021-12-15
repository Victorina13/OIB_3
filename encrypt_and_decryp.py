from generation import decryption_key
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def encryption(setting,iv):
    with open(setting['symmetric_key'], mode='rb') as key_file:
        key = key_file.read()
    ds_key = decryption_key(setting, key)
    with open(setting['initial_file'], 'r', encoding='UTF-8') as f:
        res = f.read()
    print(res)
    padder = padding.ANSIX923(64).padder()
    text = bytes(res, 'UTF-8')
    padded_text = padder.update(text) + padder.finalize()
    cipher = Cipher(algorithms.TripleDES(ds_key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    encryp_text = encryptor.update(padded_text) + encryptor.finalize()
    print("Зашифрованный текст:")
    print(encryp_text)
    with open(setting['encrypted_file'],'wb') as encryp_file:
        encryp_file.write(encryp_text)
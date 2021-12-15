from generation import generation, encryption_key, decryption_key
if __name__=='__main__':
    setting={
        'symmetric_key':'symmetric_key.txt',
        'public_key':'public_key.pem',
        'private_key':'private_key.pem',

    }
    generation(setting,16)
    encryption_key(setting)
    with open(setting['symmetric_key'], mode='rb') as key_file:
        key = key_file.read()
    ds_key = decryption_key(setting, key)
    print(ds_key)


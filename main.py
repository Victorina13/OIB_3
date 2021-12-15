from generation import generation, encryption_key
if __name__=='__main__':
    setting={
        'symmetric_key':'symmetric_key.txt',
        'public_key':'public_key.pem',
        'private_key':'private_key.pem',

    }
    generation(setting,16)
    encryption_key(setting)
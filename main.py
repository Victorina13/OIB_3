from generation import generation
if __name__=='__main__':
    setting={
        'symmetric_key':'symmetric_key.txt',
        'public_key':'public_key.pem',
        'private_key':'private_key.pem',

    }
    generation(setting,16)
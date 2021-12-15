import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
def generation(setting, key_size):
    symmetric_key = os.urandom(key_size)
    print("Symmetric key generated")
    asymmetric_keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private_key = asymmetric_keys
    public_key = asymmetric_keys.public_key()
    print("Asymmetric keys generated")
    public_pem = setting['public_key']
    with open(public_pem, 'wb') as public_out:
        public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                 format=serialization.PublicFormat.SubjectPublicKeyInfo))

    private_pem = setting['private_key']
    with open(private_pem, 'wb') as private_out:
        private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                                                    encryption_algorithm=serialization.NoEncryption()))

    with open(setting['symmetric_key'],'wb') as key_file:
        key_file.write(symmetric_key)

def encryption_key(setting):
    """шифрует симеетричный ключ открытым ключом """
    with open(setting['symmetric_key'],'rb') as key_file:
        symmetric_key=key_file.read()

    # десериализация открытого ключа
    with open(setting['public_key'], 'rb') as pem_in:
        public_bytes = pem_in.read()
    d_public_key = load_pem_public_key(public_bytes)
    symmetric_enc_key = d_public_key.encrypt(symmetric_key,padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                             label=None))
    print("Symmetric key is encrypted")
    with open(setting['symmetric_key'],'wb') as key_file:
        key_file.write(symmetric_enc_key)
    print(symmetric_key)
    print(symmetric_enc_key)

def decryption_key(setting, symmetric_key):
    with open(setting['private_key'],'rb')as pem_in:
        private_bytes=pem_in.read()
    d_private_key = load_pem_private_key(private_bytes, password=None,)
    symmetric_decryp_key = d_private_key.decrypt(symmetric_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
                                                label=None))
    print(symmetric_decryp_key)
    return symmetric_decryp_key




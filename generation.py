import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
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




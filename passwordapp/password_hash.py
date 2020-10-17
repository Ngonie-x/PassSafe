from cryptography.fernet import Fernet

def encrypt_password(password):
    key = Fernet.generate_key()
    encoded_password = password.encode()

    # encrypt the password
    f = Fernet(key)
    encrypted_password = f.encrypt(encoded_password)
    

    return encrypted_password.decode(), key.decode('utf-8')


def decrypt_password(password, key):
    password = password.encode()
    key = key.encode()
    f = Fernet(key)
    
    decrypted_password = f.decrypt(password)
    decoded_password = decrypted_password.decode()
    return decoded_password

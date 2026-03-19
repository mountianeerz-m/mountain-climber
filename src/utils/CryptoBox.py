import cryptography
import keyring
from cryptography.fernet import Fernet



class CryptoBox:
    def __init__(self, key: bytes):
        self.fernet = Fernet(key)

    def encrypt(self, value: str) -> bytes:
        return self.fernet.encrypt(value.encode())

    def decrypt(self, token: bytes) -> str:
        return self.fernet.decrypt(token).decode()


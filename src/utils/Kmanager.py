import keyring
    
from cryptography.fernet import Fernet

class KeyManager:
    def __init__(self, name):
        self.name = name
        self.SERVICE = "systm"
        

    def get(self):
        return keyring.get_password(self.SERVICE, self.name)
        

    def set(self, value):
        exist = self.get(self)
        if exist is not None:
            print(fr"key with {self.name} already exists. this will change the value of said key. ")
            keyring.set_password(self.SERVICE, self.name, value)
        else:
            keyring.set_password(self.SERVICE, self.name, value)
        
    def create_key(self):
        key = Fernet.generate_key().decode()
        
        self.set(key)
        return key
        
    def key(self):
        key = self.get()
        if key is None:
            self.create_key()
            key = self.get()
            return key
        return key

    def delete(self):
        keyring.delete_password(self.SERVICE, self.name)


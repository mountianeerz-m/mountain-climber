from src.utils.Kmanager import KeyManager
from src.utils.CryptoBox import CryptoBox




class Encrypt:
    def __init__(self, keyname, dkey=None):
        self.keyname = keyname
        self.key = KeyManager(keyname)
        self.dkey = CryptoBox(dkey) if dkey else None

    def encrypt(self, type, file, data: bytes | None = None) -> bytes:
        k = self.key.get()
        if k is None:
            print(f"Secret '{self.keyname}' not found")
            return False
        else:
            crypto = CryptoBox(k)
            if type == "file":
                try:
                    with open(file, "rb") as rfile: 
                        filedata = rfile.read()
    
                    encrypted = crypto.encrypt(filedata)
    
                    with open(file, "wb") as wfile:
                        wfile.write(encrypted)
                except Exception:
                    raise Exception

    def decrypt(self, data_type, key_type, data: bytes | None = None) -> bytes:
        if key_type == "secret":
            k = self.key.get()
            if not k:
                raise ValueError("Secret key not found")
            return CryptoBox(k).decrypt(data)

        elif key_type == "dkey":
            if not self.dkey:
                raise ValueError("dkey not configured.")
            return self.dkey.decrypt(data)

        else:
            raise ValueError(f"key type '{key_type}' not recognized")



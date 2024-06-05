import hashlib
import os
import hmac
import base64


class Hash:
    def getHash(self, string: str, salt=None):
        if salt is None:
            salt = os.urandom(16)
        dk = hashlib.pbkdf2_hmac("sha256", string.encode(), salt, 100000)
        return base64.b64encode(salt + dk).decode("utf-8")

    def verify(self, hash, string):
        decoded_data = base64.b64decode(hash)
        salt = decoded_data[:16]
        stored_dk = decoded_data[16:]
        new_dk = hashlib.pbkdf2_hmac("sha256", string.encode(), salt, 100000)
        return hmac.compare_digest(stored_dk, new_dk)

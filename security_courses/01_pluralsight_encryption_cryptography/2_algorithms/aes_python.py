from Crypto.Cipher import AES
from Crypto.Hash import MD5
from Crypto import Random
import base64

class AESCrypto:

    def __init__(self, key):
        self.key = self.md5_hash(key)

    def md5_hash(self, text):
        h = MD5.new()
        h.update(text.encode("utf-8"))
        return h.digest()

    def encrypt(self, cleartext):
        Block_Size = 16
        pad = lambda s: s + (Block_Size - len(s) % Block_Size) * chr(Block_Size - len(s) % Block_Size)
        cleartext_blocks = pad(cleartext).encode('utf-8')  # Encode padded string to bytes

        iv = Random.new().read(Block_Size)
        crypto = AES.new(self.key, AES.MODE_CBC, iv)
        encrypted = crypto.encrypt(cleartext_blocks)
        return base64.b64encode(iv + encrypted).decode('utf-8')

    def decrypt(self, enctext):
        enctext = base64.b64decode(enctext)
        iv = enctext[:16]
        crypto = AES.new(self.key, AES.MODE_CBC, iv)
        decrypted = crypto.decrypt(enctext[16:]).decode('utf-8')
        unpad = lambda s: s[:-ord(s[-1])]
        return unpad(decrypted)

aes = AESCrypto("password123")
encrypted = aes.encrypt("Hello World")
print(encrypted)
decrypted = aes.decrypt(encrypted)
print(decrypted)
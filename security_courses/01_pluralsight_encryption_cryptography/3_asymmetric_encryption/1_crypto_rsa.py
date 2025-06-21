from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto import Random
import base64

class CryptoRSA:
    PRIVATE_KEY_FILE = "private_key.pem"
    PUBLICK_KEY_FILE = "public_key.pem"

    def __init__(self):
        return

    def __save_file(self, contents, file_name):
        with open(file_name, "wb") as f:
            f.write(contents)

    def __read_file(self, file_name):
        with open(file_name, "rb") as f:
            contents = f.read()
        return contents

    def __generate_random(self):
        return Random.new().read()

    def generate_keys(self):
        keys = RSA.generate(4096)
        private_key = keys.exportKey("PEM")
        public_key = keys.public_key().exportKey("PEM")
        self.__save_file(private_key, self.PRIVATE_KEY_FILE)
        self.__save_file(public_key, self.PUBLICK_KEY_FILE)
        print("Public and Private Keys; generated and saved successfully!")

    def encrypt(self, cleartext, public_keypath=None):
        if (public_keypath==None):
            public_keypath = self.PUBLICK_KEY_FILE

        public_key = RSA.importKey(self.__read_file(public_keypath))
        cipher = PKCS1_OAEP.new(public_key)
        encrypted_data = cipher.encrypt(cleartext)
        return base64.b64encode(encrypted_data)

    def decrypt(self, cipher_text, private_key_path=None):
        if private_key_path == None:
            private_key_path = self.PRIVATE_KEY_FILE

        cipher_text = base64.b64decode(cipher_text)
        private_key = RSA.importKey(self.__read_file(private_key_path))
        cipher = PKCS1_OAEP.new(private_key)
        return cipher.decrypt(cipher_text)

crypto_rsa = CryptoRSA()
crypto_rsa.generate_keys()
encrypted_data = crypto_rsa.encrypt(cleartext="Hello World".encode("utf-8"))
print(encrypted_data)
decrypted_data = crypto_rsa.decrypt(encrypted_data)
print(decrypted_data.decode("utf-8"))




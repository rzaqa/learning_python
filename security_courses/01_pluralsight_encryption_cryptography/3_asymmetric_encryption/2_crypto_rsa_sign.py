from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_PSS
from Crypto import Random
from Crypto.Hash import SHA256
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

    def __sha256(self, input):
        sha256 = SHA256.new()
        sha256.update(input.encode("utf-8"))
        return sha256

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

    def sign(self, textmessage, private_key_path=None):
        if private_key_path == None:
            private_key_path = self.PRIVATE_KEY_FILE

        # Create private key object
        private_key = RSA.importKey(self.__read_file(private_key_path))
        # Create the signature
        signature = PKCS1_PSS.new(private_key)
        return signature.sign(self.__sha256(textmessage))

    def verify(self, signed_signature, textmessage, public_key_path=None):
        if public_key_path == None:
            public_key_path = self.PRIVATE_KEY_FILE

        # Create the public key object
        public_key = RSA.importKey(self.__read_file(public_key_path))
        # Create the verifier
        verifier = PKCS1_PSS.new(public_key)
        verification = verifier.verify(self.__sha256(textmessage), signed_signature)
        print(verification)





# crypto_rsa = CryptoRSA()
# crypto_rsa.generate_keys()
# encrypted_data = crypto_rsa.encrypt(cleartext="Hello World".encode("utf-8"))
# print(encrypted_data)
# decrypted_data = crypto_rsa.decrypt(encrypted_data)
# print(decrypted_data.decode("utf-8"))

signed_signature = CryptoRSA().sign("Hello World")
CryptoRSA().verify(signed_signature, "Hello World")


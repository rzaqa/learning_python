import hashlib

message = "Hello World"
# output = hashlib.md5(b"Hello World")
# print(output.digest)  # <built-in method digest of _hashlib.HASH object at 0x7f77cf0c8250>
# print(output)  # <md5 HASH object @ 0x7f8b1cec8250>
# print(output.hexdigest())  # b10a8db164e0754105b7a99be72e3fe5

# message = "Hello World"
# output = hashlib.md5(message.encode())
# print(output.hexdigest())  # b10a8db164e0754105b7a99be72e3fe5


def make_md5_hash_sum(phrase: str)-> str:
    output = hashlib.md5(phrase.encode())
    print(output.hexdigest())  # b10a8db164e0754105b7a99be72e3fe5
    return output.hexdigest()



make_md5_hash_sum(message)

from Crypto.Hash import HMAC

password = "secret"
byte_pass = password.encode("utf-8")
h = HMAC.new(byte_pass)
key = "Gus"
byte_key = key.encode("utf-8")
h.update(byte_key)
print(h.hexdigest()) # 7e5091084739e61def86eb991768b1ff
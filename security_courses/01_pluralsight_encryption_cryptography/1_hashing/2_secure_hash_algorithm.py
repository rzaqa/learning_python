from Crypto.Hash import SHA512

# message=b"Hello World"
#
# h = SHA512.new()
# h.update(message)
# print(h.hexdigest()) # 2c74fd17edafd80e8447b0d46741ee243b7eb74dd2149a0ab1b9246fb30382f27e853d8585719e0e67cbda0daa8f51671064615d645ae27acb15bfb1447f459b

# =================


def calculate_hash(password):
    h = SHA512.new()
    byte_pass = password.encode('utf-8')
    h.update(byte_pass)
    print(byte_pass)
    return h.hexdigest()


def subscribe(user_name, password):
    account = user_name + ":" + calculate_hash(password)
    with open('account.txt', "w") as a:
        a.write(account)
        print("[+] You are registered now")

def login(user_name, password):
    with open('account.txt', "r") as f:
        account_file = f.read()
        s = account_file.split(':')
        user_name_file = s[0]
        password_file = s[1]
        hashed_password = calculate_hash(password)

    if user_name == user_name_file and hashed_password == password_file:
        print("you are Authenticated")
    else:
        print("[!] Invalid username or password")


def main():
    user_input = input("Enter:\n 1] to subscribe\n 2] to Login\n Choice> ")
    if user_input == "1":
        user_name = input("Enter a username: ")
        password = input("Enter a password: ")
        subscribe(user_name, password)
    elif user_input == "2":
        user_name = input("Enter a username: ")
        password = input("Enter a password: ")
        login(user_name, password)
    else:
        print("[!]Invalid choice")

main()
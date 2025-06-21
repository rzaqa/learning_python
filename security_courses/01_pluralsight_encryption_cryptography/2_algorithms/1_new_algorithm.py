
def save_file(results, file_path) -> None:
    with open(file_path, "w") as f:
        f.write(results)

def open_file(file_path: str) -> str:
    with open(file_path, "r") as f:
        file_content = f.read()

    return file_content

def calculate_key(key: str) -> int:
    results = 0
    counter = 0
    #  Convert each Character into INT and added to results
    for char in key:
        counter +=1
        results += ord(char)
    return int(results/counter)

def decrypt(file_path, key):
    # Get Encrypted Text data
    file_contents = open_file(file_path)
    # Calculate the Key
    key_calc = calculate_key(key)
    dec_results = ""

    for line in file_contents:
        for wrd in line:
            for char in wrd:
                # Subtract from the Key Results
                int_char = ord(char) - key_calc
                # Append Results
                dec_results += chr(int_char)
    save_file(dec_results, file_path)
    print("[!] Finished Decryption")


def encrypt(file_path: str, key: str) -> None:
    # Get clear text data
    file_contents = open_file(file_path)
    # Calculate the Key
    key_calc = calculate_key(key)
    enc_results = ""

    for line in file_contents:
        for wrd in line:
            for char in wrd:
                # Add to the key result
                int_char = ord(char) + key_calc
                enc_results += chr(int_char)
    save_file(enc_results, file_path)
    print("[!] Finished Encryption")

def main():
    print("Please, chose in of the following: \n 1] Encrypt\n 2]Decrypt")
    choice = input(">")
    print("Enter the File Path")
    file_path = input(">")
    print("Enter the Secret Key")
    key = input(">")
    #Encrypt
    if choice == "1":
        encrypt(file_path, key)
    #Decrypt
    elif choice == "2":
        decrypt(file_path, key)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()


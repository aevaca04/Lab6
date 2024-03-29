def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit \n")

def encode(decoded):
    empty_str = ""
    for i in decoded:
        if i == "7":
            i = "0"
        if i == "8":
            i = "1"
        if i == "9":
            i = "2"
        else:
            i = int(i)
            i += 3
            i = str(i)
        empty_str += i
    return empty_str

def decode(encoded):  # this is encode defintion  # this is done by partner Alexis
        decode_encoded = ""
        for num in encoded:
            decode_encoded = decode_encoded + str((int(num) - 3) % 10)
            return decode_encoded


def main():
    encoder = True
    menu()
    while encoder == True:
        user_option = int(input("Please enter an option: "))
        if user_option == 1:
            original_pass = input("Please enter your password to encode: ")
            encoded_password = encode(original_pass)
            print("Your password has been encoded and stored!")
            menu()
        if user_option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            menu()  # prints menu
        if user_option == 3:
            encoder = False
if __name__ == '__main__':
    main()

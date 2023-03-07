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

def decode(encoded):
    pass

def main():
    encoder = True
    menu()
    while encoder == True:
        user_option = int(input("Please enter an option: "))
        if user_option == 1:
            original_pass = input("Please enter your password to encode: ")
            encoded_password = encode(origial_pass)
            print("Your password has been encoded and stored!")
            menu()
        if user_option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_pass}.") #decoded_pass is not a thing yet
            menu()

if __name__ == '__main__':
    main()
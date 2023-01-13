
#This function will go over each character of the text, convert it into ASCII, shifts it, and converts it back to an encrypted text.
def encrypt():
    encrypted_text = ("ENCRYPTED TEXT: ")
    for char in text:
        x = ord(char)
    #Checks if the text is written using the alphabet, shifts them, and converts it into text.
        if char.isalpha() == True:
            encrypted_text += chr(x+key)
    #Check if 
        elif char.isdigit() == True:
            encrypted_text += chr(x)
        else:
            encrypted_text += char
    print(encrypted_text)
    encrypted_text = ""
def decrypt():
    decrypted_text = ("DECRYPTED TEXT: ")
    for char in text:
        x = ord(char)
    #Checks if the text is written using the alphabet, shifts them, and converts it into text.
        if char.isalpha() == True:
            decrypted_text += chr(x-key)
    #Check if 
        elif char.isdigit() == True:
            decrypted_text += chr(x)
        else:
            decrypted_text += char
    print(decrypted_text)
    decrypted_text = ""

print("WELCOME TO THE MI6 ENCRYPTOR")
#This will allow the program to run infinitly
while True:
    #This part of the code is where the agent will enter their provided message to transmit "securely"

    text = input("ENTER PROVIDED TEXT: ")
    key = int(input("ENTER PROVIDED KEY: "))
    choice = input("ENCRYPT OR DECRYPT [e/d]: ").lower()
    if choice == "e":
        encrypt()
    else:
        decrypt()

#Imports time library for the loading feature
import time
#This function is added for loading and waiting.
def loading():
        #Uses the time library to enable sleeping.
        time.sleep(0.75)
#This function will go over each character of the text, convert it into ASCII, shifts it, and converts it back to an encrypted text.
def encrypt():
    #This is a string variable for the final output
    encrypted_text = ""
    #Goes through each character
    for char in text:
        #Converts those characters into ASCII
        x = ord(char)
        #Checks if the text is written using the alphabet, shifts them, and converts it into text.
        if char.isalpha() == True:
            #Checks for uppercase characters and shifts them
            if char.isupper() == True:
                encrypted_text += chr(65+(x-65+key)%(26))
            else:
            #Checks for lowercase characters and shifts them
                encrypted_text += chr(97+(x-97+key)%(26))
        #Check for numbers, and does not shift them
        elif char.isdigit() == True:
            encrypted_text += chr(x)
        else:
        #Checks for characters, symbols, and signs, and does not shift them
            encrypted_text += char
    #Prints the encrypted text
    print("ENCRYPTED TEXT: ",encrypted_text)
    #Used to seperate each session
    print("================================================================================")
    #Clears the encrypted_text variable for next session
    encrypted_text = ""
#This function will decrypt the text if a key is provided.
def decrypt():
    #This is also string variable for the final output
    decrypted_text = ""
    #Goes through each character
    for char in text:
        #Converts those characters into ASCII
        x = ord(char)
    #Checks if the text is written using the alphabet, shifts them, and converts it into text.
        if char.isalpha() == True:
            if char.isupper() == True:
                decrypted_text += chr(65+(x-65-key)%(26))
            else:
                decrypted_text += chr(97+(x-97-key)%(26))
        #Check for numbers, and does not shift them
        elif char.isdigit() == True:
            decrypted_text += chr(x)
        else:
        #Checks for characters, symbols, and signs, and does not shift them
            decrypted_text += char
    #Prints the decrypted text along with the key
    print("[",key,"] ","DECRYPTED TEXT: ",decrypted_text)
    #Used to seperate each session
    print("================================================================================")
    decrypted_text = ""
#This function will brute force the text without a key by giving out all the combinations
def brute():
    #This allows the key variable to be accessible by every function
    global key
    #Sets the key variable to 0
    key = 0
    #Goes through all possible combinations
    for key in range(26):
        #Itterates from 1 to 26
        key += 1
        loading()
        #The decrypt function is used to save time, 
        decrypt()
#Print a welcome message to the user
print("========================= WELCOME TO THE MI6 ENCRYPTOR==========================")
#This section of the code is where the agent will enter their provided message to transmit "securely"
def program():
        #This will allow the program to run infinitly
        while True:
            #Makes the text variable accessible by all the functions
            global text
            #Makes the key variable accessible by all the functions
            global key
            #Enter the text they want to encrypt/decrypt
            text = input("ENTER PROVIDED TEXT: ")
            #Decides whether to decrypt or encrypt
            choice = input("ENCRYPT OR DECRYPT [e/d]: ").lower()
            #This choice will allow the user to encrypt their text with a key
            if choice == "e":
                #This indicates how much the user wants to shift
                key = int(input("ENTER PROVIDED KEY: "))
                print("ENCRYPTING...")
                #Added loading for realism.
                loading()
                #Calls the encrypt function
                encrypt()
            #If the user enters anything else, the program will automatically assume they want to decrypt.
            else:
                #Ask if the user has the key to decrypt
                key_state = input("Do you have a key [y/n]? ").lower()
                #If yes, they enter a key
                if key_state == "y":
                    #This also indicates how much the user wants to shift
                    key = int(input("ENTER PROVIDED KEY: "))
                    #This shows that the user's input is being decrypted
                    print("DECRYPTING...")
                    #Adds realism and trust to the user
                    loading()
                    #Calls the decrypt function
                    decrypt()
                #If not, the program will try every combination of keys
                else:
                    #Calls in the brute-force function
                    brute()
program()

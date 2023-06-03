import random
import string

chars = "Ü" + "Ö" + "Ş" + "Ç" + "Ğ" + "İ" + "ü" + "ö" + "ş" + "ç" + "ğ" + "ı" + " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

choice=input("Encrypt or Decryprt. (E/D)")
if choice in "E":
    omessage = input("Enter your message: ")
    ecmessage = ""
    for letter in omessage:
        index = chars.index(letter)
        ecmessage += key[index]
    print(f"Encrypted message: {ecmessage}")
    def convert(key):
        dkey = ""
        for x in key:
            dkey += x
        return dkey
    print("Key: ", convert(key))
    input("Enter any key to exit!")
    
elif choice in "D":
    ecmessage = input("Enter your message: ")
    key = input("Enter your key: ")
    omessage = ""
    for letter in ecmessage:
        index = key.index(letter)
        omessage += chars[index]
    print(f"Original message: {omessage}")
    input("Enter any key to exit!")
        
else:
    print('Are you an idiot?')
    input("Enter any key to exit!")
    
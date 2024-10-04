#Here we are taking a list that is alphabet list
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#this encryption function code is for to encrypt or to convert plain text to cipher text
def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            char_position=alphabet.index(char)
            new_position=(char_position+shift_key)%26 #this is the formula
            cipher_text += alphabet[new_position]
        else:#this is for numbers,special symbols etc
            cipher_text += char
    print("your Encrypted Text : ",cipher_text) #required text

#this decryption function code is for to decrypt or to convert cipher text to plain text
def decryption(cipher_text, shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabet:
            char_position = alphabet.index(char)
            new_position = (char_position - shift_key) % 26 #this is the formula
            plain_text += alphabet[new_position]
        else:#this is for numbers,special symbols etc
            plain_text +=char
    print("your Decrypted Text : ", plain_text) #required text

end=False #initializing with False
while not end: #True
    choice=input("type 'encrypt' for encryption and type 'decrypt' for decryption\n")
    text=input("Type your message:\n")
    key=int(input("Enter your shift key")) # shift key for encryption and decryption
    # Note: key should be same for encryption and decryption
    if choice=='encrypt':
        encryption(text,key) # encryption function call
    elif choice=='decrypt':
        decryption(text,key) # decryption function call

    want_end=input("Enter 'yes' to continue , 'no' to exit")
    if want_end=='no':
        print("I hope it was comfortable and efficient to you! ,Thank you! Bye") # end msg
        end=True
    elif want_end=='yes':
        end=False


def caesar_cipher():
    message = str(input("Enter your message: "))
    while message.isascii() != True:
        message = str(input("Please enter only ASCII characters! "))
    message = message.replace(" ", "")
    shift = int(input("Enter the shift of the cipher (must be an integer): "))
    encrypted_message = ""
    for character in message:
        encrypted_message += chr(32 + ((ord(character) - 32 + shift) % 95))
    return encrypted_message

def cc_decrypt(): 
    message = str(input("Enter your message: "))
    shift = int(input("Enter shift: "))
    unencrypted_message = ""
    for character in message:
        unencrypted_message += chr(32 + ((ord(character) - 32 - shift) % 95)) 
    return unencrypted_message

answer = caesar_cipher()
print(answer)
decrypt = cc_decrypt()
print(decrypt)
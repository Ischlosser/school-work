def caesar_cipher():
    message = str(input("Enter your message: "))
    while message.isascii() != True:
        message = str(input("Please enter only ASCII characters! "))
    shift = int(input("Enter the shift of the cipher (must be an integer): "))
    encrypted_message = ""
    for character in message:
        x = ord(character)
        encrypted_message += chr(32 + (x + shift) % (127 - 32))
    return encrypted_message

answer = caesar_cipher()
print(answer)
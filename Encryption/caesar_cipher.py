def caesar_cipher():
    message = str(input("Enter your message: "))
    while message.isascii() != True:
        message = str(input("Please enter only ASCII characters! "))
    shift = input("Enter the shift of the cipher (must be an integer): ")
    while shift.is_integer() != True:
        shift = str(input("Please enter only ASCII characters! "))
    encrypted_message = ""
    for character in message:
        x = ord(character)
        encrypted_message += chr(32 + (x + shift) % (127 - 32))
    return encrypted_message

answer = caesar_cipher()
print(answer)
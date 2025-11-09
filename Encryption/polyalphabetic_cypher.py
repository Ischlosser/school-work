def polyCypher(): 
    message = str(input("Enter your message: "))
    message = message.replace(" ", "")
    shift = input("Enter the shift word of the cipher (must be ASCII): ")
    shift = shift.replace(" ", "")
    enc_text = ""
    shift_list = list(str(shift))
    i = 0
    for character in message:
        if i == len(shift):
          i = 0
        enc_text += chr(ord(character) + ord(shift_list[i]))
        i += 1
    print(enc_text)

def polyCypherDecrypt(): 
    message = str(input("Enter your message: "))
    shift = input("Enter the shift word of the cipher (must be ASCII): ")
    shift = shift.replace(" ", "")
    dec_text = ""
    shift_list = list(str(shift))
    i = 0
    for character in message:
        if i == len(shift):
          i = 0
        dec_text += chr(ord(character) - ord(shift_list[i]))
        i += 1
    print(dec_text)

polyCypher()
polyCypherDecrypt()
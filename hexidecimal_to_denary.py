def hextodenary(hex_string):
    value = 0
    power = 0
    
    for i in reversed(hex_string):  
        if '0' <= i <= '9':
            digit_value = int(i)
        elif 'A' <= i <= 'F':
            digit_value = 10 + (ord(i) - ord('A'))
        elif 'a' <= i <= 'f': 
            digit_value = 10 + (ord(i) - ord('a'))
        else:
            return "cannot convert"
        
        value += digit_value * (16 ** power) 
        power += 1
        
    return value

h = input("Please enter a hex: ")
print(hextodenary(h))

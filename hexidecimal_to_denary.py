def hextodenary(hex): #this needs to be fixed !!!!
    value = 0
    power = 0
    for i in reversed(hex):
        if '0' <= i <= '9':
            digit_value = int(i)
        elif 'A' <= i <= 'F':
            digit_value = 10 + (ord(i)-ord('A'))
        else:
            return "cannot convert"
        
        value = digit_value * (16 ** power)
        power += 1
    return value

h = str(input("Please enter a hex: "))
print(hextodenary(h))
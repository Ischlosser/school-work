def binarytodenary(binary):
    power = 0
    value = 0
    if len(binary) != 8:
        return "Please enter exactly 8 bits"
 
    for i in range(len(binary) -1, -1, -1):
        if binary[i] == '1':
           value += 2 ** power
        power += 1    
    return value
n = input("Please enter binary: ")
print(binarytodenary(n))  
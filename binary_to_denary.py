def binarytodenary(binary):
    power = 0
    value = 0
    for i in range(len(binary) -1, -1, -1):
        if binary[i] == '1':
           value += 2 ** power
        power += 1    
    return value
n = input("Please enter binary: ")
print(binarytodenary(n))  
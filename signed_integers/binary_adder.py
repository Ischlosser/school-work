def addition(n, k, x):
    if len(n) != 8:
        return "Please enter exactly 8 bits"
    if len(k) != 8:
        return "Please enter exactly 8 bits"
    if x == 1:
        result = ""
        carry = 0 
        for i in range(7, -1, -1):
            total = int(n[i]) + int(k[i]) + carry
            if total == 0:
                result = '0' + result
                carry = 0
            elif total == 1:
                result = '1' + result
                carry = 0
            elif total == 2:
                result = '0' + result
                carry = 1
            else:  
                result = '1' + result
                carry = 1
        if carry == 1:
            result = '1' + result
        if len(result) != 8:
            return "Overflow error"  
        return result 
    elif x == 2:
        k = twoscomp_sign(k)
        result = ""
        carry = 0
        for i in range(7, -1, -1):
            total = int(n[i]) + int(k[i]) + carry
            if total == 0:
                result = '0' + result
                carry = 0
            elif total == 1:
                result = '1' + result
                carry = 0
            elif total == 2:
                result = '0' + result
                carry = 1
            else:  
                result = '1' + result
                carry = 1 
        if len(result) != 8:
            return "Overflow error"               
        return result
    else:
        return "invalid input" 

def twoscomp_sign(n):
    result = ""
    flag = False 
    for i in range(7, -1, -1):  
        if not flag:           
            result = n[i] + result
            if n[i] == '1':
                flag = True
        else:            
            if n[i] == '1':
                result = '0' + result
            else:
                result = '1' + result

    return result

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

def checking(n, k, a, x):
    n1 = binarytodenary(n)
    n2 = binarytodenary(k)
    if x == 1:
        answer = n1 + n2
        answer2 = binarytodenary(a)
        if answer == answer2:
            return "Correct"
        else: 
            return "False"
    elif x == 2:
        answer = n1 - n2
        answer2 = binarytodenary(a)
        if answer == answer2:
            return "Correct"
        else: 
            return "False"
  
x = int(input("Would you like to add or subtract (Add = 1, Subtract = 2)"))
n = input("Please enter first binary: ")
k = input("Please enter second binary: ")
a = addition(n, k, x)
print(addition(n, k, x))
print(checking(n, k, a, x))
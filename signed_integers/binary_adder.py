def addition(n, k):
    if len(n) != 8:
        return "Please enter exactly 8 bits"
    if len(k) != 8:
        return "Please enter exactly 8 bits"
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
    return result      
n = input("Please enter first binary: ")
k = input("Please enter second binary: ")
print(addition(n, k))
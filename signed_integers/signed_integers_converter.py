def twoscomplent(binary):
    if len(binary) != 8:
        return "Please enter exactly 8 bits"
    
    value = int(binary, 2)

    if binary[0] == '1':
        value -= 1 << 8  
    
    return value

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

 

n = input("Please enter binary: ")
print(twoscomp_sign(n))
    
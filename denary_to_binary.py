numbertoconvert = int(input("Enter a number to convert: "))

def number_converter(n):
    if 0 <= n <= 255:
        
        binary = ""
        
        for i in range(8):
            binary = str(n%2) + binary
            n = n // 2
        return binary    
    else:
        return "cannot convert" 
    
print(number_converter(numbertoconvert)) 
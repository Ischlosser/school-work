def counting(digit, n):
    n -= 1
    print(digit)
    digit += 1
    if n <= 0:
        return ""
    else:
        counting(digit, n)

def iterCount(n):
    result = 0
    counter = 1
    while counter <= n:
        result = result+1 
        counter += 1
        print(result)
    return ""

      
number = int(input("How high would you like to count? "))
print(counting(1, number))   
print(iterCount(number))

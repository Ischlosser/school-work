print("factorial")

def iterFact(n):
    result = 1
    counter = 1
    while counter <= n:
        result = result * counter
        counter += 1
    return result

def recursiveFact(n):
    if n > 0:
        result = recursiveFact(n-1)*n
    else:
        result = 1    
    return result


nFact = int(input("Enter whole number:"))    
print("Factorial =", str(iterFact(nFact)))
print("Factorial: ", recursiveFact(nFact))
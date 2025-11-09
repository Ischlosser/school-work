def Fib(x, y, n):
    z = x + y
    print(str(z))
    n -= 1
    if n <= 1:
        return 
    else:
        Fib(y, z, n)

def iterFib(n):
    x = 0 
    y = 1
    for i in range(0, n):
        if i <= 1:
            print(i)
        else:
            result = x + y
            x = y 
            y = result
            print(result)
    return        

number = int(input("Please enter the digit you'd like to count to: "))
print("Recursive Fibonacci Sequence")
print(str(0))
print(str(1))
Fib(0, 1, number-1)
print("Iterative Fibonacci Sequence")  

iterFib(number)    

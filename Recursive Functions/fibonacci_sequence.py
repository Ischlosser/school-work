def Fib(x, y, n):
    z = x + y
    print(str(z))
    n -= 1
    if n <= 1:
        return 
    else:
        Fib(y, z, n)

print(str(0))
print(str(1))
Fib(0, 1, 1000000000000)        

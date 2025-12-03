def swapping(x, y):
    x, y = y, x
    return x, y
while True:
    a = input("Input first variable (a): ")
    b = input("Input second variable (b): ")
    print(f"a originally: {a}, b originally: {b}")
    a, b = swapping(a, b)
    print(f"a swapped: {a}, b swapped: {b}")
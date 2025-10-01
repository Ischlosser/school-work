def counting (digit, n):
    n -= 1
    print(digit)
    digit += 1
    if n <= 0:
        return "Finished"
    else:
        counting(digit, n)

number = int(input("How high would you like to count? "))
print(counting(1, number))        
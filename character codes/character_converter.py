max = int(input("Enter a minimum: "))
min = int(input("Enter a maximum: "))

for i in range(max-min, -1):
    print(chr(i))
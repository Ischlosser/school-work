max_value = int(input("Enter a minimum: "))
min_value = int(input("Enter a maximum: "))

for i in range(min_value, max_value + 1):
    char = chr(i)
    print(f"{i} -> {char}")
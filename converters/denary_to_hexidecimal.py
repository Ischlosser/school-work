def denarytohexadecimal(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")

    return hex(number)[2:].upper()

n = int(input("Please enter an integer:"))
print(denarytohexadecimal(n)) 
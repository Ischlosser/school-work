def linSearch(search):
    count = 0
    fruit = ["Pear", "Apple", "Banana", "Orange", "Lemon"]
    try:
        while fruit:
            if search == fruit[count]:
                print(f"{search} found at index {count}! Tries: {count+1}")
                return
            else:
                print(f"Found {fruit[count]}, trying again.")
                count += 1
    except IndexError:
        print("Fruit is not in list.")
            
while True:
    print("------------------------------------------------")
    print("What would you like to search for?")
    print("List: Pear, Apple, Banana, Orange, Lemon")
    linSearch(input("Enter: "))

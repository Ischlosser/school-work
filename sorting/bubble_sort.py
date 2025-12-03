import random

def bubble_sort(items):
    print(f"Unsorted list: {items}")
    swaps = 0
    swapped = False
    while swapped == False:
        swapped = True
        for i in range(len(items)-1):
            if items[i] < items[i+1]:
                pass 
            elif items[i] > items[i+1]:
                items[i], items[i+1] = items[i+1], items[i]
                swaps += 1
                swapped = False
            else:
                pass
    print(f"Sorted list: {items}")
    print(f"{swaps} swaps was needed")

while True:
    names = ["Sviatoslav", "Filip", "Anna", "Joseph", "Alfie", "Emily", "Adela", "Matvii", "Xuanbin", "Alexandra", "Ester", "Anastasiia", "Radovan"]
    print("What list would you like to use: ")
    print(f"1: Unshuffled list: {names} ")
    shuffled_names = random.sample(names, len(names))
    print(f"2: Shuffled list: {shuffled_names}")
    a = input("Enter: ")
    if a == 'break':
        break
    try: #I learned about this way of error and I am trying to use it here
        a = int(a)
        if a == 1:
            bubble_sort(names)
        elif a == 2: 
            bubble_sort(shuffled_names)
    except ValueError as error:
        print("Error, try again")
    print("-------------------------------------------------------------")

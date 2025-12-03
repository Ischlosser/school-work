import random

def insertion_sort(names):
    comparisons = 0
    accesses = 0
    for i in range(1, len(names)):
        accesses += 1
        for j in range(i):
            comparisons += 1
            if names[i] < names[j]:
                names.insert(j, names.pop(i))
                break
            else:
                pass
    print(f"Sorted names: {names}")
    print(f"Comparisons: {comparisons}")
    print(f"Accesses: {accesses}")

while True:
    names = ["Sviatoslav", "Filip", "Anna", "Joseph", "Alfie", "Emily", "Adela", "Matvii", "Xuanbin", "Alexandra", "Ester", "Anastasiia", "Radovan"]
    print("What list would you like to use: ")
    print(f"1: Unshuffled list: {names} ")
    shuffled_names = random.sample(names, len(names))
    print(f"2: Shuffled list: {shuffled_names}")
    a = input("Enter: ")
    if a == 'break':
        break
    try: 
        a = int(a)
        if a == 1:
            insertion_sort(names)
        elif a == 2: 
            insertion_sort(shuffled_names)
    except ValueError as error:
        print("Error, try again")
    print("-------------------------------------------------------------")

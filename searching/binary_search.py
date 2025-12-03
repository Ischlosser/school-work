import math, time

def iterative_binary_search(search):
    start = time.time()
    names = ['Amirpasha', 'Arman', 'Denis', 'Farid', 'Imre', 'Lekai', 'Leo', 'Noel', 'Vadim']
    count = 0 
    low = 0
    high = len(names) - 1
    while low <= high:
        count += 1
        jump = (low + high) // 2
        if names[jump] == search:
            print(f"{names[jump]} found at index {jump}! Count: {count}")
            print(time.time() - start)
            return        
        elif search < names[jump]:
            print(f"Found {names[jump]}, trying again.")
            high = jump - 1        
        else:
            print(f"Found {names[jump]}, trying again.")
            low = jump + 1

    print(f"{search} is not in list.")


            

def recursive_binary_search(search, count, lst, ido, index):   

    if len(lst) == 0:
        print(f"{search} not found.")
        return None

    start = time.time()
    count += 1
    jump = math.floor((len(lst)-1) / 2)
    index += jump

    if search == lst[jump]:
        print(f"{lst[jump]} found at index {index}! Count: {count}")
        print(ido)
        return index
    elif search < lst[jump]:
        print(f"Found {lst[jump]}, trying again.")
        new_lst = lst[:jump]      
        ido += time.time() - start
        return recursive_binary_search(search, count, new_lst, ido, index - jump)
    else:
        print(f"Found {lst[jump]}, trying again.")
        new_lst = lst[jump+1:]    
        ido += time.time() - start
        return recursive_binary_search(search, count, new_lst, ido, index + 1)


def main():
    iterative_binary_search(input("Enter name you are searching for: "))
    recursive_binary_search(input("Enter name you are searching for: "), 0, ['Amirpasha', 'Arman', 'Denis', 'Farid', 'Imre', 'Lekai', 'Leo', 'Noel', 'Vadim'], 0, 0)

if __name__ == "__main__": 
    while True:
        main()
import random
dies = int(input("How many dies would you like to roll? "))
rolls = int(input("How many times would you like to roll?"))

def rolling(dies, rolls):
    roll = []
    results = [[] for _ in range(6*dies)]
    for i in range(rolls):
        for j in range(dies):
            roll.append(random.randint(1, 6))
        print(roll)
        print(sum(roll))
        results[sum(roll)+1].append(sum(roll))
        roll = []
    for i in range(6*dies): #fix this 
        print(f"The amount of {i-1} is {len(results[i])}")


rolling(dies, rolls)
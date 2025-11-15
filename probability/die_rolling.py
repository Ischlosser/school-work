import random, csv
import matplotlib.pyplot as mpl

dies = int(input("How many dies would you like to roll? "))
rolls = int(input("How many times would you like to roll? "))

def rolling(dies, rolls):
    roll = []
    final = [[f"{q}"] for q in range(6*dies+2)]
    results = [[] for _ in range(6*dies+2)]
    for k in range(rolls):
        for j in range(dies):
            roll.append(random.randint(1, 6))
        #print(roll)
        #print(sum(roll))
        results[sum(roll)+1].append(sum(roll))
        roll = []
    for i in range(dies, 6*dies+1): 
        final[i].append(len(results[i+1]))
        print(f"The amount of {i} is {len(results[i+1])}")
    #print(results)
    with open("die_rolling_stats.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Sum", "Frequency"])
        for l in range(dies, 6 * dies+1):
            writer.writerow(final[l])
        writer.writerow(["Rolls", rolls])
    mpl.title(f'Frequency of Sums from Rolling {dies} Dice ({rolls} Rolls)')
    mpl.xlabel('Sum of Dice')
    mpl.ylabel('Frequency')
    for x in range(dies, 6*dies+1):
        mpl.plot(final[i][0], final[i][1], marker='o', linestyle='-', color='b')
    mpl.xticks([p for p in range(6*dies+2)]) #needs fix
    mpl.show()




rolling(dies, rolls)
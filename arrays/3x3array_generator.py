import random
columns = int(input("Enter a number of columns: ")) 
rows = int(input("Enter a number of rows: "))
grid = [[0 for _ in range(columns)] for _ in range(rows)]
used_numbers = set()
for r in range(rows):
    for c in range(columns):
        rand = random.randint(1, rows*columns)        
        while True:
            rand = random.randint(1, rows*columns)
                        
            if rand not in used_numbers:              
                break
        grid[r][c] = rand
        used_numbers.add(rand)

for row in grid:
    print(row)
  
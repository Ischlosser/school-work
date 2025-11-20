import random

def rotate_90_cw(matrix):
    return ((matrix[1][0], matrix[0][0]), (matrix[1][1], matrix[0][1]))

def rotate_90_ccw(matrix):
    return ((matrix[0][1], matrix[1][1]), (matrix[0][0], matrix[1][0]))

def rotate_180(matrix):
    return ((matrix[1][1], matrix[1][0]), (matrix[0][1], matrix[0][0]))

def swap(matrix, i, j):
    flat = list(matrix[0] + matrix[1])
    flat[i], flat[j] = flat[j], flat[i]
    return (tuple(flat[0:2]), tuple(flat[2:4]))

def get_neighbors(matrix):
    neighbors = []
    neighbors.append((rotate_90_cw(matrix), "Rotate 90° CW"))
    neighbors.append((rotate_90_ccw(matrix), "Rotate 90° CCW"))
    neighbors.append((rotate_180(matrix), "Rotate 180"))
    swaps = [(0,1), (1,3), (2,3), (0,2)]
    for i, j in swaps:
        neighbors.append((swap(matrix, i, j), "Swap positions " + str(i) + " and " + str(j)))
    return neighbors

def matrix_to_str(matrix):
    return ''.join([str(n) for row in matrix for n in row])

def bfs(start, goal):
    visited = set()
    queue = [(start, [])]
    visited.add(matrix_to_str(start))

    while queue:
        current, path = queue.pop(0)
        if current == goal:
            return path + [(current, "Goal reached!")]

        for neighbor, action in get_neighbors(current):
            key = matrix_to_str(neighbor)
            if key not in visited:
                visited.add(key)
                queue.append((neighbor, path + [(neighbor, action)]))
    return None

def print_matrix(matrix):
    print("[" + str(matrix[0][0]) + " " + str(matrix[0][1]) + "]")
    print("[" + str(matrix[1][0]) + " " + str(matrix[1][1]) + "]")


def new_arrengeing_algorithm():
    global LB, RB, LF, RF, L1, L2, R1, R2
    start_matrix = ((LB, RB), (LF, RF))
    goal_matrix = ((L1, L2), (R1, R2))

    print(start_matrix)
    print(goal_matrix)

    steps = bfs(start_matrix, goal_matrix)

    if not steps:
        return
    #if len(steps) >= 3:
    #    await spinner(90)


    # Execute steps
    print("Steps to reach goal:\n")
    print("Start Matrix:")
    print_matrix(start_matrix)
    print()

    for i, (matrix, action) in enumerate(steps, 1):
        print("Step " + str(i) + ": " + action)
        print_matrix(matrix)
        #print("# Insert robotic arm command for:", action)
        """print("# Example: robot.rotate_90_cw() or robot.swap(0, 1)\n")
        if i == 2 and action == "Swap positions 2 and 3":
            await motor.run_to_relative_position(port.A, 0, 200)
            await spinner(-180)                
            await lifter(145)               
            await straigth(11.5, 500, 500)  
            await straigth(-2.7)            
            await lifter(-155, 200, 100, 400)
            await shake()
        elif i == 2:
            await motor.run_to_relative_position(port.A, -90, 200)
            await lifter(145)
            await straigth(5)
            await lifter(-145, 100)
            await shake()
        else:
            if action == "Rotate 90° CCW":
                await spinner(90)
            elif action == "Rotate 90° CW":
                await spinner(-90)
            elif action == "Rotate 180":
                await spinner(180)
            elif action == "Swap positions 0 and 1":
                await spinner(180)
                await backmix()
                await spinner(-180)
            elif action == "Swap positions 2 and 3":
                await backmix()
            elif action == "Swap positions 0 and 2":
                await spinner(90)
                await backmix()
                await spinner(-90)
            elif action == "Swap positions 1 and 3":
                await spinner(-90)
                await backmix()
                await spinner(90)"""

colors1 = [3, 6, 7, 9]
colors2 = [3, 6, 7, 9]

LB = random.choice(colors1)
colors1.remove(LB)
RB = random.choice(colors1)
colors1.remove(RB)
LF = random.choice(colors1)
colors1.remove(LF)
RF = random.choice(colors1)
colors1.remove(RF)

L1 = random.choice(colors2)
colors2.remove(L1)
R1 = random.choice(colors2)
colors2.remove(R1)
L2 = random.choice(colors2)
colors2.remove(L2)
R2 = random.choice(colors2)
colors2.remove(R2)

new_arrengeing_algorithm()
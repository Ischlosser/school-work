stack_subjects = []
queue_subjects = []
def push():
    obj = input("Please enter element: ")
    stack_subjects.append(obj)
    if len(stack_subjects) > 10:
        stack_subjects.pop()
        print(stack_subjects)
        return "Stack Overflow"
    return stack_subjects

def pop():
    if not stack_subjects:
        return "Stack Underflow"
    else:
        popped = stack_subjects.pop()
        print("Subject popped: " + str(popped))
        return stack_subjects

def peek():
    return stack_subjects[-1]


def enqueue():
    obj = input("Please enter element: ")
    queue_subjects.append(obj)
    if len(queue_subjects) > 10:
        queue_subjects.pop()
        return "Queue Overflow"
    return queue_subjects

def dequeue():
    if not queue_subjects:
        return "Queue Underflow"
    else:
        dequeued = queue_subjects.pop(0)
        print("Subject dequeued: " + str(dequeued))
        return queue_subjects

while True:
    print("####################")
    print("Would you like to: ")
    print("1: Push")
    print("2: Pop")
    print("3: Peek")
    print("4: Enqueue")
    print("5: Dequeue")
    a = input("Enter: ")
    print("####################")
    print()
    if int(a) == 1:
        print(push())
    elif int(a) == 2:
        print(pop())
    elif int(a) == 3:
        print(peek())
    elif int(a) == 4:
        print(enqueue())
    elif int(a) == 5:
        print(dequeue())
    else:
        print("Invalid Input")
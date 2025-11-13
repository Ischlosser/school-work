stack_subjects = ["", "", "", "", "", "", "", "", "", ""]
queue_subjects = ["", "", "", "", "", "", "", "", "", ""]
slast = 0
qfirst = 0
qlast = 0
def push():
    global slast
    if slast >= 10:
        print(stack_subjects)
        return "Stack Overflow"
    else:
        stack_subjects[slast] = input("Please enter element: ")
        slast += 1
        return stack_subjects

def pop():
    global slast
    if slast == 0:
        return "Stack Underflow"
    else:
        print("Subject popped: " + stack_subjects[slast-1])
        stack_subjects[slast-1] = ""
        slast -= 1
        return stack_subjects

def peek():
    return stack_subjects[slast-1]


def enqueue():
    global qlast
    if qlast >= 10:
        
        return "Queue Overflow"
    queue_subjects[qlast] = input("Please enter element: ")
    qlast += 1
    return queue_subjects

def dequeue(): 
    global qfirst, qlast
    if qfirst == qlast:
        qfirst = 0
        qlast = 0
        return "Queue Underflow"
    else:
        print("Dequeued "+ queue_subjects[qfirst])
        queue_subjects[qfirst] = ""
        qfirst += 1
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
    if a == "1":
        print(push())
    elif a == "2":
        print(pop())
    elif a == "3":
        print(peek())
    elif a == "4":
        print(enqueue())
    elif a == "5":
        print(dequeue())
    else:
        print("Invalid Input")
    print(" ")
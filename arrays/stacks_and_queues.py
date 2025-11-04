def stack():
    subjects = []
    for i in range(10):
        subject = input(f"Enter subject #{i+1} (max. 10, enter 'finished' to stop): ")
        if subject.lower() == 'finished':
            break
        subjects.append(subject)
        print(subjects)
    while subjects:
        pop = subjects.pop()
        print(pop)
    return subjects

def queue():
    subjects = []
    for i in range(10):
        subject = input(f"Enter subject #{i+1} (max. 10, enter 'finished' to stop): ")
        if subject.lower() == 'finished':
            break
        subjects.append(subject)
        print(subjects)
    while subjects:
        dequeued_subject = subjects.pop(0)
        print(dequeued_subject)
    return subjects

while True:
    a = 0
    a = int(input("Would you like to queue(0) or stack(1) your subjects? "))
    if a == 0:
        queue()
    elif a == 1:
        stack()
    else:
        print("Bad input, try again")
class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

def listCreator(root, previous, newNode):
    global start
    
    if newNode.data.lower() < root.data.lower():
        newNode.next = root
        newNode.previous = previous
        if previous:
            previous.next = newNode
        root.previous = newNode
        return

    if root.next is not None:
        listCreator(root.next, root, newNode)
    else:
        root.next = newNode
        newNode.previous = root
    return

def listTraversal(current, start):
    print(current.data)
    if current.next == start:
        return
    listTraversal(current.next, start)

start = input("Enter root node: ")
start = Node(str(start))

while True:
    newNode = input("Enter name of next node: ")
    if newNode == "traverse":
        last = start
        while last.next is not None:
            last = last.next
        last.next = start
        start.previous = last
        listTraversal(start, start) 
    elif newNode == "break":
        break  
    else:
        listCreator(start, start.previous, Node(newNode))  

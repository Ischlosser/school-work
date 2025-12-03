class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None
        self.checked = False


def listCreator(root, previous, newNode):
    global start  

    if newNode.data.lower() < root.data.lower():
        newNode.next = root
        newNode.previous = previous
        if previous:
            previous.next = newNode
        root.previous = newNode
        start = newNode
        return

    if root.next is not None:
        listCreator(root.next, root, newNode)
    else:
        root.next = newNode
        newNode.previous = root


def listTraversal(current, start):
    print(current.data)
    if current.next == start:
        return
    listTraversal(current.next, start)


def listRetrieval(current):
    if current.checked:
        return
    current.checked = True
    listRetrieval(current.previous)
    print(current.data)


start = input("Enter root node: ")
start = Node(start)

while True:
    newNode = input("Enter name of next node: ")

    if newNode == "traverse":
        last = start
        while last.next is not None:
            last = last.next
        last.next = start
        start.previous = last

        print("Forward traversal:")
        listTraversal(start, start)

        curr = start
        while True:
            curr.checked = False
            curr = curr.next
            if curr == start:
                break

        print("Reverse retrieval:")
        listRetrieval(last)  

    elif newNode == "break":
        break

    else:
        listCreator(start, None, Node(newNode))

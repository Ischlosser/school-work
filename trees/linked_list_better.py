class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

home = Node("Home")

def ListTraversal(node):
    node = home.next 
    if not node:
        print("List is empty")
        return
    
    while node:
        print(node.data)
        node = node.next

def ListRetrieval(node):
    node = home.next
    if not node:
        print("List is empty")
        return
    while node.next:
        node = node.next  
    while node and node.data != "Home":
        print(node.data)
        node = node.previous

def NodeCreation(newNode):
    current = home.next
    if current is None:
        home.next = newNode
        newNode.previous = home
        return
    while current and current.data.lower() < newNode.data.lower():
        current = current.next
    if current is None:
        tail = home
        while tail.next:
            tail = tail.next
        tail.next = newNode
        newNode.previous = tail
        return
    prev = current.previous
    newNode.next = current
    newNode.previous = prev
    prev.next = newNode
    current.previous = newNode

def NodeDeletion(name):
    node = home.next
    while node:
        if node.data == name:
            prev = node.previous
            nxt = node.next

            prev.next = nxt
            if nxt:
                nxt.previous = prev

            print(f"Deleted: {name}")
            return

        node = node.next

    print("Node not found.")

while True:
    print("Options: ")
    print("1: Create new Node")
    print("2: Delete Node")
    print("3: Traverse (In Order)")
    print("4: Traverse (Reverse Order)")
    print("Type 'break' to exit.")
    
    a = input("Enter: ")

    if a == 'break':
        break
    a = int(a)
    if a == 1:
        name = input("Please enter new Node name: ")
        NodeCreation(Node(name))
    elif a == 2:
        name = input("Please enter node to be deleted: ")
        NodeDeletion(name)
    elif a == 3:
        ListTraversal(home)
    elif a == 4:
        ListRetrieval(home)
    else:
        print("Error, try again.")

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def treeBuilding(nodeName, root):
    if nodeName.lower() < root.data.lower():
        if root.left is None:
            root.left = TreeNode(nodeName)
        else:
            treeBuilding(nodeName, root.left)
    else:
        if root.right is None:
            root.right = TreeNode(nodeName)
        else:
            treeBuilding(nodeName, root.right)

def treePrinting(root):
    if root is None:
        return
    left = root.left.data if root.left else "None"
    right = root.right.data if root.right else "None"
    print(f"Node {root.data} has left node {left} and right node {right}")
    treePrinting(root.left)
    treePrinting(root.right)

def inOrderTrav(node):
    if node:
        inOrderTrav(node.left)
        print(node.data)
        inOrderTrav(node.right)

def preOrderTrav(node):
    if node:
        print(node.data)
        preOrderTrav(node.left)
        preOrderTrav(node.right)

def postOrderTrav(node):
    if node:
        postOrderTrav(node.left)
        postOrderTrav(node.right)
        print(node.data)

counter = 0
root = input("Enter root node: ")
root = TreeNode(str(root))
while True:
    newNode = input("Enter name of next node: ")
    treeBuilding(newNode, root)
    counter += 1
    if counter % 6 == 0:
        print("How would you like to traverse the tree:")
        print("1: In order")
        print("2: Pre order")
        print("3: Post order")
        a = input("Enter: ")
        if int(a) == 1:
            inOrderTrav(root)
        elif int(a) == 2:
            preOrderTrav(root)
        elif int(a) == 3:
            postOrderTrav(root)
        print("Would you like to print the tree?")
        print("1: Yes")
        print("2: No")
        b = input("enter: ")
        if int(b) == 1:
            treePrinting(root)
        elif int(b) == "break":
            break
        else:
            print("Okay (will ask again in 6 inputs)")
        
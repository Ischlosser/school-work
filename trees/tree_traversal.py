class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

imre = TreeNode('Imre')
farid = TreeNode('Farid')
lekai = TreeNode('Lekai')
jaymes = TreeNode('Jaymes')
vadim = TreeNode('Vadim')
jacob = TreeNode('Jacob')
raphael = TreeNode('Raphael')

imre.left = farid
imre.right = lekai

lekai.left = jaymes
lekai.right = vadim

jaymes.left = jacob

vadim.left = raphael

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

while True:
    print("#########################################")
    print("How would you like to traverse the tree:")
    print("1: In order")
    print("2: Pre order")
    print("3: Post order")
    a = input("Enter: ")
    if int(a) == 1:
        inOrderTrav(imre)
    elif int(a) == 2:
        preOrderTrav(imre)
    elif int(a) == 3:
        postOrderTrav(imre)
    elif int(a) == 4:
        break
    else:
        print("Error try again")
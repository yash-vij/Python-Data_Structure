class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key

n = Node(12)
n.left = Node(20)
n.right = Node(30)
n.left.left = Node(54)
print("Data of Root node : ",n.data)
print("Data of left child : ",n.left.data)
print("Data of right child :",n.right.data)
print("Data of left child of left child of root node: ",n.left.left.data)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_node(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data," -> ",end=" ")
            temp = temp.next

    def reverse_list(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


llist = Linked_list()
llist.insert_node(10)
llist.insert_node(20)
llist.insert_node(30)
llist.insert_node(40)
llist.print_list()
llist.reverse_list()
print()
print("Reversed List is : ")
llist.print_list()
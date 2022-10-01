class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def inser_at_front(self,front_data) :
        new_node = Node(front_data)

        new_node.next = self.head
        self.head = new_node

llist = linked_list()
llist.inser_at_front(3)
llist.inser_at_front(4)
llist.inser_at_front(5)
llist.inser_at_front(6)
llist.print_list()

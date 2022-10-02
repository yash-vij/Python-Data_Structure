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

    def insert_after(self, previous, new_data):
        count = 0
        if previous == None:
            print("Previous cannot be empty")
            return

        new_node =  Node(new_data)
        new_node.next = previous.next
        previous.next = new_node

    def insert_last(self, new_data):
        ele = llist.head
        while(ele.next != None):
            ele = ele.next
        new_node = Node(new_data)
        ele.next = new_node


llist = linked_list()
llist.inser_at_front(3)
llist.inser_at_front(4)
llist.inser_at_front(5)
llist.inser_at_front(6)
llist.insert_after(llist.head.next.next, 100)
llist.insert_after(llist.head.next.next, 1345)
llist.insert_last(45)
llist.insert_last(98)
llist.print_list()


class Node :
    def __init__(self,data = None):
        self.data = data
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp :
            print(temp.data)
            temp = temp.next

llist = Linked_List()
llist.head = Node(1)
second = Node(3)
third = Node(4)
llist.head.next = second
second.next = third
llist.print_list()

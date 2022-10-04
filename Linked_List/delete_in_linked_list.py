class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_list :
    def __init__(self):
        self.head = None

    def delete_front(self):
        temp = self.head.data
        self.head = self.head.next
        print("Deleted data is : ",temp)

    def inser_at_front(self, front_data):
        new_node = Node(front_data)

        new_node.next = self.head
        self.head = new_node

    def print_List(self):
        temp = self.head
        while temp.next!=None:
            print(temp.data)
            temp = temp.next

llist = Linked_list()

llist.inser_at_front(23)
llist.inser_at_front(12)
llist.inser_at_front(234)
llist.inser_at_front(324)
llist.inser_at_front(120)
llist.inser_at_front(1)

llist.delete_front()

llist.print_List()




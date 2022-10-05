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
        print("Deleted data from front is : ",temp)

    def delete_last(self):
        temp = self.head.next
        while(temp.next != None):
            temp = temp.next
        if(temp.next == None):
            temp.next = None
        print("Deleted data from last is : ", temp.data)

    def delete_at_location(self,position):
        if self.head is None:
            return
        index = 0
        current = self.head
        while current.next and index < position:
            previous = current
            current = current.next
            index += 1

        if index == 0:
            self.head = self.head.next

        else:
            previous.next = current.next


    def inser_at_front(self, front_data):
        new_node = Node(front_data)

        new_node.next = self.head
        self.head = new_node

    def print_List(self):
        temp = self.head
        while temp.next!=None:
            print(temp.data,"->",end=" ")
            temp = temp.next

llist = Linked_list()


llist.inser_at_front(1)
llist.inser_at_front(2)
llist.inser_at_front(3)
llist.inser_at_front(4)
llist.inser_at_front(5)
llist.inser_at_front(6)

llist.delete_front()
llist.delete_last()
llist.delete_at_location(2)
llist.print_List()




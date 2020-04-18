class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_last(self, data):
        n = Node(data)
        n.next = None
        if self.head == None:
            self.head = n
        else:
            p = self.head
            while(p.next != None):
                p = p.next

            p.next = n

    def insert_first(self, data):
        n = Node(data)
        if(self.head == None):
            self.head = n
        else:
            n.next = self.head
            head = n

    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    def size(self):
        c = 0
        p = self.head
        while(p != None):
            c += 1
            p = p.next
        return c


    def insert(self, data, index):
        n = Node(data)
        if(self.isempty()):
            self.head = n
        else:
            if(index == 0):
                n.next = self.head
                self.head = n

            elif(index>0 and index<=self.size()):
                p = self.head
                for i in range(index-1):
                    p = p.next
                n.next = p.next
                p.next = n

            else:
                print("index out of bound")


    def max_int(self):
        p = self.head.next
        max = self.head.data
        while(p.next != None):
            if p.data > max:
                max = p.data
            p = p.next

        return max

    def display(self):
        p = self.head
        print("the linked list is: ", end = " ")
        while(p != None):
            print(f"{p.data}", end=" ")
            p = p.next
        print("\n")

    def l_to_ll(self, l):
        ll_1 = LinkedList()
        for i in l:
            ll_1.insert_last(i)
        return ll_1

    def delete_node(self, index):
        if self.head == None:
            print("No element is present")
        else:
            if(index == 0):
                self.head = self.head.next
            elif(index>0 and index<self.size()):
                q = None
                p = self.head
                for i in range(index):
                    q = p
                    p = p.next
                q.next = p.next
                p = None
            else:
                print("index out of bound")

    def reverse(self):
        r = self.head
        q = r.next
        p = q.next
        




# ll = LinkedList()
# ll.insert_last(10)
# ll.insert_last(100)
# ll.insert_last(50)
# ll.display()
# # ll.insert_last(67)
# # ll.display()
# print(ll.size(), end = "\n")
#
# ll.insert(33, 2)
#
# ll.display()

l = [8, 89, 56, 99]
ll=LinkedList()
ll_11 = ll.l_to_ll(l)
ll_11.display()
ll_11.delete_node(0)
ll_11.display()

# print(ll.size())

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linked:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_at_begin(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            node=Node(data)
            node.next=self.head
            self.head=node
            
    
    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data)
        else:
            node=Node(data)
            temp=self.tail
            temp.next=node
            self.tail=node
    


    def print_values(self):
        #print("Hi")
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
#        print(temp.data)
    def print_reverse(self):
        prev=None
        while self.head:
            temp=self.head
            self.head=self.head.next
            temp.next=prev
            prev=temp
        self.head=prev
        self.print_values()


t=linked()
t.insert_at_begin(5)
t.insert_at_begin(10)
t.insert_at_end(15)
t.insert_at_end(20)

t.print_values()
t.print_reverse()
class node:
    def __init__(self,val):
        self.val=val
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def add_back(self,val):
        if self.head==None:
            self.head=node(val)
            self.tail=self.head
        else:
            self.tail.next=node(val)
            self.tail=self.tail.next
        self.length+=1
    def remove_front(self):
        res=self.head.val
        self.head=self.head.next
        self.length-=1
        return res
    def print_list(self):
        curr=self.head
        lst=[]
        while curr is not None:
            lst.append(curr.val)
            curr=curr.next
        print(lst)
    def get_front(self):
        return self.head.val


a=linkedlist()

a.add_back(1)
a.add_back(2)
a.remove_front()
a.print_list()
print(a.length)

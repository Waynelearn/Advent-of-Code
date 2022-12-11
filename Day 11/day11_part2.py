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


class monkey:
    def __init__(self,name,start_items,operation,test_factor,val_if_true,val_if_false):
        self.name=name
        self.start_items=start_items
        self.operation=operation
        self.test_factor=test_factor
        self.val_if_true=val_if_true
        self.val_if_false=val_if_false
        
        self.num_of_inspection=0
        
    def inspect(self):
        
        if self.start_items.length==0:
            return None,None
        self.num_of_inspection+=1
        #print(f"Monkey {self.name} inspects {self.start_items[0]}")
        #print(f"OPERATE ON 2:{self.operation(2)}")
        self.start_items.head.val=self.operation(self.start_items.get_front())
        #print(f"Worry level change to {self.start_items[0]}")

        
        
        #print(f"Monkey gets bored, worry level change to {self.start_items[0]}")
        if self.start_items.get_front()%self.test_factor==0:
            next_monkey=self.val_if_true
        else:
            next_monkey=self.val_if_false
        #print(f"Moneky {self.name} give {self.start_items[0]} to Monkey {next_monkey}")
        return next_monkey, self.start_items.remove_front()%(2*3*5*7*11*13*17*19)
    
    def recieve(self,item):
        if item is None:
            pass
        self.start_items.add_back(item)
        
class round:
    def __init__(self,monkies):
        self.monkies=monkies
        self.curr_round=1
    def start(self):
        for monkey in self.monkies:
            while monkey.start_items.length!=0:
                next_monkey,item=monkey.inspect()
                self.monkies[next_monkey].recieve(item)
        self.curr_round+=1

def operation_gen(operator,operand):
        if operator=="*":
            if operand == "old":
                op = lambda x:x*x
            else:
                op = lambda x:x*int(operand)
        elif operator=="+":
            if operand == "old":
                op = lambda x:x+x
            else:
                op = lambda x:x+int(operand)
        return op
with open("input.txt") as f:
    data=f.readlines()

    
monkey_lst=[]

idx=0
for line in data:
    line=line.strip("\n")
    line=line.split(" ")
    
    if idx%7==0:
        name=int(line[1][:-1])
    elif idx%7==1:
        items=[int(i.strip(",")) for i in line[4:]]
        temp = linkedlist()
        for item in items:
            temp.add_back(item)
    elif idx%7==2:
        operator=line[6]
        operand=line[7]
    elif idx%7==3:
        test_factor =int(line[-1])
        #print(f"test_factor:{test_factor}")
    elif idx%7==4:
        val_if_true=int(line[-1])
        #print(f"val if true:{val_if_true}")
    elif idx%7==5:
        val_if_false=int(line[-1])
        #print(f"val if false:{val_if_false}")
        op=operation_gen(operator,operand)
        m = monkey(name,temp,op,test_factor,val_if_true,val_if_false)
        monkey_lst.append(m)
        

    idx+=1




sim=round(monkey_lst)


    
for i in range(10000):
    sim.start()
inspec=[]
for m in sim.monkies:
    print(m.num_of_inspection)
    inspec.append(m.num_of_inspection)
    #m.start_items.print_list()
inspec=sorted(inspec)
print(inspec[-1]*inspec[-2])



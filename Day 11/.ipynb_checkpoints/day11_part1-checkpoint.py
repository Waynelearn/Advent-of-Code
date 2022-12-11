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
        self.num_of_inspection+=1
        if len(self.start_items)==0:
            return None,None
        self.start_items[0]=self.operation(self.start_items[0])
        self.start_items[0]=self.start_items[0]//3
        if self.start_items[0]%self.test_factor==0:
            next_monkey=self.val_if_true
        else:
            next_monkey=self.val_if_false
        
        return next_monkey, self.start_items.pop(0)
    
    def recieve(self,item):
        if item is None:
            pass
        self.start_items.append(item)
        
class round:
    def __init__(self,monkies):
        self.monkies=monkies
        self.curr_round=1
    def start(self):
        for monkey in self.monkies:
            next_monkey,item=monkey.inspect()
            if next_monkey is None:
                pass
            else:
                self.monkies[next_monkey].recieve(item)
        self.curr_round+=1
        
with open("input1.txt") as f:
    data=f.readlines()

    
monkey_lst=[]

idx=0
for line in data:
    line=line.strip("\n")
    line=line.split(" ")
    print(line)
    if idx%7==0:
        name=int(line[1][:-1])
    elif idx%7==1:
        items=[int(i.strip(",")) for i in line[4:]]
        print(items)
    elif idx%7==2:
        operator=line[6]
        operand=line[7]
        if operator=="*":
            if operand == "old":
                operation = lambda x:x*x
            else:
                operation = lambda x:x*int(operand)
        elif operator=="+":
            if operand == "old":
                operation = lambda x:x+x
            else:
                operation = lambda x:x+int(operand)
    elif idx%7==3:
        test_factor =int(line[-1])
    elif idx%7==4:
        val_if_true=int(line[-1])
    elif idx%7==5:
        val_if_false=int(line[-1])
        m = monkey(name,items,operation,test_factor,val_if_true,val_if_false)
        monkey_lst.append(m)
        

    idx+=1

sim=round(monkey_lst)
for i in range(20):
    sim.start()

for m in sim.monkies:
    print(m.name,m.start_items,m.num_of_inspection)
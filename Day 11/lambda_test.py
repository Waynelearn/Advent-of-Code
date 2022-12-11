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
        
        if len(self.start_items)==0:
            return None,None
        self.num_of_inspection+=1
        #print(f"Monkey {self.name} inspects {self.start_items[0]}")
        #print(f"OPERATE ON 2:{self.operation(2)}")
        self.start_items[0]=self.operation(self.start_items[0])
        #print(f"Worry level change to {self.start_items[0]}")
        
        self.start_items[0]=self.start_items[0]//3
        #print(f"Monkey gets bored, worry level change to {self.start_items[0]}")
        if self.start_items[0]%self.test_factor==0:
            next_monkey=self.val_if_true
        else:
            next_monkey=self.val_if_false
        #print(f"Moneky {self.name} give {self.start_items[0]} to Monkey {next_monkey}")
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
            while len(monkey.start_items)!=0:
                next_monkey,item=monkey.inspect()
                if next_monkey is None:
                    break
                else:
                    self.monkies[next_monkey].recieve(item)
        self.curr_round+=1

        return op
with open("input1.txt") as f:
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
    elif idx%7==2:
        operator=line[6]
        operand=line[7]
        if operator=="*":
            if operand == "old":
                op = lambda x:x*x
            else:
                operand=int(operand)
                op = (lambda a:lambda x:x*a)(operand)
        elif operator=="+":
            if operand == "old":
                op = lambda x:x+x
            else:
                operand=int(operand)
                op = (lambda a:lambda x:x+a)(operand)
    elif idx%7==3:
        test_factor =int(line[-1])

        #print(f"test_factor:{test_factor}")
    elif idx%7==4:
        val_if_true=int(line[-1])
        #print(f"val if true:{val_if_true}")
    elif idx%7==5:
        val_if_false=int(line[-1])
        #print(f"val if false:{val_if_false}")
        m = monkey(name,items,op,test_factor,val_if_true,val_if_false)
        monkey_lst.append(m)
    if idx>=2:
        print(f"operator:{operator}")
        print(f"operand:{operand}")
    if idx>=5:
        print(f"operation on 5:{op(5)}")
    for m in monkey_lst:
        print(f"idx:{idx},name:{m.name},m.operation(5):{m.operation(5)}")
        

    idx+=1

sim=round(monkey_lst)
for i in range(20):
    sim.start()

for m in sim.monkies:
    print(m.name,m.start_items,m.num_of_inspection)



class directory():
    def __init__(self,name):
        self.name=name
        self.size=0
        self.parent=None
        self.children=[]

def file():
    def __init__(self,name,size):
        self.name=name
        self.size=size
        self.parent=None
with open("input1.txt","r") as f:
    lines=[]
    for line in f:
        lines.append(line.strip("\n").split())

for i in range(len(lines)):
    

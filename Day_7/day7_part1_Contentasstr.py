def p(action,txt):
    print(f"[{action}] {txt}")

def sep():
    print("___________________________________________________________________")
class directory():
    def __init__(self):
        self.name=None
        self.size=0
        self.parent=None
        self.dir=[]
        self.files=[]
    def get_name(self):
        return self.name
    def get_size(self):
        return self.size
    def get_parent(self):
        return self.parent
    def set_name(self,name):
        self.name=name
    def set_size(self,size):
        self.size=size
    def set_parent(self,parent):
        p("SETTING PARENT",f"Parent of DIR {self.name} set to {parent.name}")
        self.parent=parent
    def update_size(self,size):
        size=int(size)
        p("UPDATING SIZE",f"Size of {self.name} is updated from {self.size} to {self.size+size}")
        self.size+=size
        if self.parent!=None:
            self.parent.update_size(size)
    def add_content(self,content):
        if isinstance(content,file):
            p("ADDING FILE",f"File {content.name} is added to directory {self.name}")
            self.files.append(content.name)
        elif isinstance(content,directory):
            p("ADDING DIR",f"Directory {content.name} is added to directory {self.name}")
            self.dir.append(content.name)
        #add size
        self.update_size(content.size)
        

class file():
    def __init__(self):
        self.name=None
        self.size=0
        self.parent=None
    def get_name(self):
        return self.name
    def get_size(self):
        return self.size
    def get_parent(self):
        return self.parent
    def set_name(self,name):
        self.name=name
    def set_size(self,size):
        self.size=size
    def set_parent(self,parent):
        p("SETTING PARENT",f"Parent of FILE {self.name} set to {parent.name}")
        self.parent=parent
        

class file_system():
    def __init__(self):
        self.root=directory()
        self.root.set_name("/")
        self.curr_dir=self.root
        #shows all directory
        self.directories={}
    def create_dir(self,d):
        temp=directory()
        temp.set_name(d)
        p("CREATE DIR",f"Name:{d}")
                
        
        #update parent
        temp.set_parent(self.curr_dir)
        self.directories[(temp.name,temp.parent)]=temp
        #add the directory in the cwd
        self.curr_dir.add_content(temp)


        return temp
    def create_file(self,size,f):
        temp=file()
        temp.set_name(f)
        temp.set_size(size)
        p("CREATE FILE",f"Size:{size},Name:{f}")
        #update parent
        temp.set_parent(self.curr_dir)
        #update the cwd
        self.curr_dir.add_content(temp)

        
    def cd(self,d):
        if d=="/":
            p("GO TO ROOT",f"From {self.curr_dir.get_name()}")
            self.curr_dir=self.root
        #get parent directory
        elif d=="..":
            p("GO TO PARENT DIR",f"From {self.curr_dir.name} To {self.curr_dir.get_parent().name}")
            self.curr_dir=self.curr_dir.get_parent()
        #regular directory
        else:
            #add unseen dir
            if self.directories.get((d,self.curr_dir.name)) is None:
                #create the new unseen directory
                temp=self.create_dir(d)
                #set cwd to dir
                self.curr_dir=temp
                p("CHANGE UNKNOWN DIR",f"From {self.curr_dir.name} To {temp.name}")
            else:
                p("CHANGE KNOWN DIR",f"From {self.curr_dir.name} To {self.directories.get(d).name}")
                self.curr_dir=self.directories.get((d,self.curr_dir.name))
        sep()
    def ls(self,children):
        #list of tuples
        for child in children:
            first=child[0]
            second=child[1]
            if first=="dir" and second not in self.curr_dir.dir:
                self.create_dir(second)
            elif first!="dir" and second not in self.curr_dir.files:
                self.create_file(first,second)
        sep()
with open("input.txt","r") as f:
    file_system=file_system()
    prev_ls=False
    while True:
        if prev_ls==False:
            line=f.readline().strip("\n").split(" ")
        p("CURRENT LINE",f"{line}")
        if len(line)==1:
            break
        first=line[0]
        
        if first=="$":
            cmd = line[1]
            if cmd=="ls":
                temp=[]
                p("LIST",f"{line}")
                nextline=f.readline().strip("\n").split(" ")
                p("NEXT LINE",f"{nextline}")
                nextfirst=nextline[0]
                while nextfirst != "$":
                    temp.append(nextline)
                    #continue reading
                    nextline=f.readline().strip("\n").split(" ")
                    nextfirst=nextline[0]
                    #no more lines
                    if len(nextline)==1:
                        break
                #next cmd is reached
                line=nextline
                prev_ls=True
                    
                file_system.ls(temp)
            elif cmd=="cd":
                prev_ls=False
                file_system.cd(line[2])
total=0
for val in file_system.directories.values():
    if val.size<=100000:
        total+=val.size
p("Number of DIR",f"{len(file_system.directories.keys())}")
p("ROOT SIZE",f"{file_system.root.size}")
p("Total Sum",f"{total}")
used=file_system.root.size
required=30000000
freespace=70000000-used
space_needed=required-freespace

m=9999999999999
min_d=None

for i,val in file_system.directories.items():
    d,p=i[0],i[1]

    if val.size<m and val.size>space_needed:
        m=val.size
        min_d=d
print(m)
print(d)
        





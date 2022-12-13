def p(action,txt):
    print(f"[{action}] {txt}")

def sep():
    print("___________________________________________________________________")
class directory():
    def __init__(self):
        self.name=None
        self.size=0
        self.parent=None
        self.contents=[]
    def get_name(self):
        return self.name
    def get_size(self):
        return self.size
    def get_parent(self):
        return self.parent
    def get_contents(self):
        return self.contents
    def set_name(self,name):
        self.name=name
    def set_size(self,size):
        self.size=size
    def set_parent(self,parent):
        p("SETTING PARENT",f"Parent of DIR {self.name} set to {parent.name}")
        self.parent=parent
    def set_contents(self,contents):
        self.contents=contents
    def update_size(self,size):
        size=int(size)
        p("UPDATING SIZE",f"Size of {self.name} is updated from {self.size} to {self.size+size}")
        self.size+=size
        if self.parent!=None:
            self.parent.update_size(size)
    def add_content(self,content):
        if isinstance(content,file):
            p("ADDING FILE",f"File {content.name} is added to directory {self.name}")
        elif isinstance(content,directory):
            p("ADDING DIR",f"Directory {content.name} is added to directory {self.name}")
        #content can be file or folder
        self.contents.append(content)
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
                
        self.directories[d]=temp
        #add the directory in the cwd
        self.curr_dir.add_content(temp)
        #update parent
        temp.set_parent(self.curr_dir)

        return temp
    def create_file(self,size,f):
        temp=file()
        temp.set_name(f)
        temp.set_size(size)
        p("CREATE FILE",f"Size:{size},Name:{f}")
        #update the cwd
        self.curr_dir.add_content(temp)
        #update parent
        temp.set_parent(self.curr_dir)
        
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
            if self.directories.get(d) is None:
                #create the new unseen directory
                temp=self.create_dir(d)
                #set cwd to dir
                self.curr_dir=temp
                p("CHANGE UNKNOWN DIR",f"From {self.curr_dir.name} To {temp.name}")
            else:
                p("CHANGE KNOWN DIR",f"From {self.curr_dir.name} To {self.directories.get(d).name}")
                self.curr_dir=self.directories.get(d)
        sep()
    def ls(self,children):
        #list of tuples
        for child in children:
            first=child[0]
            second=child[1]
            if first=="dir":
                self.create_dir(second)
            else:
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
                    p("LIST CONTENT",f"{nextline}")
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
for key in file_system.directories.keys():
    if file_system.directories[key].get_size()<=100000:
        total+=file_system.directories[key].get_size()
print(total)

def mapping_alpha_to_num(a):
    return ord(a)-ord("a")

grid=[]
with open("input.txt","r") as f:
    for line in f:
        grid.append(line.strip("\n"))


max_row=len(grid)-1
max_col=len(grid[0])-1
for line in grid:
    print(line)
#print(max_row)
#print(max_col)
class point:
    def __init__(self,row,col,val):
        self.row=row
        self.col=col
        self.val=val
        self.start=False
        self.end=False

    def passable(self,other_val):
        if self.val>other_val:
            if self.val-other_val>1:
                return False
            else:
                return True
        else:
            return True

            
        
class bfs:
    def __init__(self,num_rows,num_cols):
        self.num_rows=num_rows
        self.num_cols=num_cols
        self.grid=[["*" for i in range(num_cols) ] for j in range(num_rows)]
        self.start=None
        self.end=None
        self.visit_grid=[["_" for i in range(num_cols) ] for j in range(num_rows)]

    def neighbours(self,row,col):
        lst=[]
        #up
        if row-1<=max_row and row-1>=0 and self.grid[row][col].passable(self.grid[row-1][col].val):
            lst.append(self.grid[row-1][col])
        #down
        if row+1<=max_row and row+1>=0 and self.grid[row][col].passable(self.grid[row+1][col].val):
            lst.append(self.grid[row+1][col])
        #right
        if col+1<=max_col and col+1>=0 and self.grid[row][col].passable(self.grid[row][col+1].val):
            lst.append(self.grid[row][col+1])
        #left
        if col-1<=max_col and col-1>=0 and self.grid[row][col].passable(self.grid[row][col-1].val):
            lst.append(self.grid[row][col-1])
        return lst
        
    def search(self):
        step=1
        visited=[]
        curr=self.start
        queue=self.neighbours(self.start.row,self.start.col)
        temp=len(queue)
        counter=0
        print(f"Initial Queue:{[(q.row,q.col) for q in queue]}")
        while len(queue)!=0:
            if curr.val==0:
                print("end reached")
                break
            #visited
            visited.append(curr)
            self.visit_grid[curr.row][curr.col]="#"
            #for line in self.visit_grid:
                #print("".join(line))
            print(f"[VISIT] Row:{curr.row},Col:{curr.col}")
            #get next
            curr=queue.pop(0)
            #add next point's neighbours
            for pt in self.neighbours(curr.row,curr.col):
                if pt not in visited and pt not in queue:
                    print(f"[QUEUEING] Row:{pt.row},Col:{pt.col}")
                    queue.append(pt)
            counter+=1
            print(f"counter:{counter},step:{step},temp:{temp},queue len:{len(queue)},queue len-temp:{len(queue)-temp}")
            if counter==temp:
                step+=1
                temp=len(queue)
                counter=0
        return step
        
            
            

bfs=bfs(len(grid),len(grid[0]))

for row in range(len(grid)):
    for col in range(len(grid[row])):
        #if start or end
        curr=grid[row][col]
        if curr=="S":
            p=point(row,col,mapping_alpha_to_num("a"))
            bfs.grid[row][col]=p
        elif curr=="E":
            p=point(row,col,mapping_alpha_to_num("z"))
            bfs.grid[row][col]=p
            bfs.start=p
        else:
            p=point(row,col,mapping_alpha_to_num(grid[row][col]))
            bfs.grid[row][col]=p
for i in range(max_row+1):
    line=[]
    for j in range(max_col+1):
        line.append(bfs.grid[i][j].val)
    print(line)

print(bfs.search())





    

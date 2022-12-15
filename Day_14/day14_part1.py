import re

with open("input.txt","r") as f:
    data=[i for i in f]

padding=0

max_x=0
min_x=1000000
max_y=0
stone_x=[]
stone_y=[]
for line in data:
    pattern_y=r",([\d]{1,3})"
    pattern_x=r"([\d]{1,3}),"
    #print(line)
    x=[int(i) for i in re.findall(pattern_x,line)]
    y=[int(i) for i in re.findall(pattern_y,line)]
    stone_x.append(x)
    stone_y.append(y)
    print(x)
    print(y)
    if max(x)>max_x:
        max_x=max(x)
        
    if min(x)<min_x:
        min_x=min(x)

    if max(y)>max_y:
        max_y=max(y)
print(f"[MAX X]:{max_x}")
print(f"[MIN X]:{min_x}")
print(f"[MAX Y]:{max_y}")


grid = [["_" for i in range(max_x-min_x+1)] for i in range(max_y+1+padding)]

def p():
    x_cor=[str(i) for i in range(max_x-min_x+1)]
    x_cor="".join(x_cor)
    
    print("______________________________[GRID]______________________________")
    print(" ",x_cor)
    for i,line in enumerate(grid):
        print(i,"".join(line))
    print("______________________________[GRID]______________________________")


def mapping(x,min_x):
    return x-min_x

stones=[]
for i in range(len(stone_x)):
    temp_x=[mapping(j,min_x) for j in stone_x[i]]
    stones.append(list(zip(temp_x,stone_y[i])))
    #print("stone",stones[i])
for stone in stones:
    for i in range(len(stone)):
        #print(stone[i])
        x=stone[i][0]
        y=stone[i][1]
        if i==0:
            #start
            #print(f"[STARTING] x:{x},y:{y}")
            curr_x=x
            curr_y=y
            grid[curr_y][curr_x]="#"
        while curr_x!=x or curr_y!=y:
            dir_x=x-curr_x
            dir_y=y-curr_y
            #print(f"[BEFORE MOVE] curr_x:{curr_x},curr_y:{curr_y}")
            if dir_x>0:
                curr_x+=1
            elif dir_x<0:
                curr_x-=1
                
            if dir_y>0:
                curr_y+=1
            elif dir_y<0:
                curr_y-=1            
            #print(f"[AFTER MOVE] curr_x:{curr_x},curr_y:{curr_y}")
            grid[curr_y][curr_x]="#"
            #p()


p()

print(f"[SAND SPAWN AT x:{mapping(500,min_x)}]")
spawn=mapping(500,min_x)

x_limit=max_x-min_x
y_limit=len(grid)-1
print(x_limit)
print(y_limit)


def spawn_sand(grid,spawn):
    curr_x=spawn
    curr_y=0
    #simulate falling
    while True:
        if curr_y+1>y_limit or curr_y<0 or curr_x<0 or curr_x+1>x_limit:
            return True

        
        #fall downwards
        if grid[curr_y+1][curr_x]=="#" or grid[curr_y+1][curr_x]=="O":
            #blocked
            
            
            #check left down
            if grid[curr_y+1][curr_x-1]=="_":
                curr_x-=1
                curr_y+1
            elif grid[curr_y+1][curr_x+1]=="_":
                curr_x+=1
                curr_y+=1
            else:
            #check right down
                grid[curr_y][curr_x]="O"
                #p()
                
                return False
            #p()
        else:
            curr_y+=1
            #grid[curr_y][curr_x]="v"
            #p()
            #grid[curr_y][curr_x]="_"
idx=0    
while not spawn_sand(grid,spawn):
    idx+=1
p()

print(idx)



with open("input.txt","r") as f:
    grid = list(f.readlines())
    grid = [[int(i) for i in line.strip("\n") ] for line in grid]


#for line in grid:
    #print(line)
row=len(grid)
col=len(grid[0])


def out_of_bound(curr_row,curr_col,row,col):
    if curr_row>=row or curr_row<0:
        return True
    elif curr_col>=col or curr_col<0:
        return True
    else:
        return False
def check_top(grid,curr_row,curr_col,row,col,val,count):
    """
    Check if the top edge can be reached
    """
    new_row,new_col=curr_row-1,curr_col
    if out_of_bound(new_row,new_col,row,col):
        return count
    else:
        #check if i can go top, next < now
        if grid[new_row][new_col]<val:
            return check_top(grid,new_row,new_col,row,col,val,count+1)
        else:
            return count+1

def check_down(grid,curr_row,curr_col,row,col,val,count):
    """
    Check if the down edge can be reached
    """
    new_row,new_col=curr_row+1,curr_col
    if out_of_bound(new_row,new_col,row,col):
        return count
    else:
        #check if i can go top, next < now
        if grid[new_row][new_col]<val:
            return check_down(grid,new_row,new_col,row,col,val,count+1)
        else:
            return count+1
def check_right(grid,curr_row,curr_col,row,col,val,count):
    """
    Check if the right edge can be reached
    """
    
    new_row,new_col=curr_row,curr_col+1
    #print(f"new:{new_row},{new_col}:{out_of_bound(new_row,new_col,row,col)}")
    if out_of_bound(new_row,new_col,row,col):
        return count
    else:
        #check if i can go top, next < now
        if grid[new_row][new_col]<val:
            return check_right(grid,new_row,new_col,row,col,val,count+1)
        else:
            return count+1
def check_left(grid,curr_row,curr_col,row,col,val,count):
    """
    Check if the top edge can be reached
    """
    new_row,new_col=curr_row,curr_col-1
    
    if out_of_bound(new_row,new_col,row,col):
        return count
    else:
        #check if i can go top, next < now
        if grid[new_row][new_col]<val:
            return check_left(grid,new_row,new_col,row,col,val,count+1)
        else:
            return count+1

def check(grid,curr_row,curr_col,row,col,val):
    return check_top(grid,curr_row,curr_col,row,col,val,0)*check_down(grid,curr_row,curr_col,row,col,val,0)*check_right(grid,curr_row,curr_col,row,col,val,0)*check_left(grid,curr_row,curr_col,row,col,val,0)


total=0
res=[[0 for i in range(col)] for j in range(row)]

for r in range(row):
    for c in range(col):
        res[r][c]=check(grid,r,c,row,col,grid[r][c])
print(max([max(r) for r in res]))
"""
for r in range(row):
    print(res[r])

#print(check_right(grid,3,1,row,col))
"""

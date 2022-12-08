
"""
a line of drawing
3 char to represent inventory
1 space between inventory
11 char = 3*3 inventory = 9 char, 2 spaces

a single line with \n marks the end of drawing
"""

with open("input.txt","r") as f:
    
    #add all the inventory
    line_num=0
    
    for line in f:
        if line_num==0:
            first=line.strip("\n")
            box_num=(len(first)+1)//4
            inventory={i:[] for i in range(1,box_num+1)}
        for index in range(len(line)):
            if line[index].isalpha():
               stack_index=(index-1)//4 + 1 #offset of 4 between inv,1 for [
               print(f"[ADDING] Box {line[index]} to stack {stack_index}")
               inventory[stack_index].append(line[index])
               


        line_num+=1
    
        if line=="\n":
            break
    #invert the inventory
    for key in inventory.keys():
        print(f"[BEFORE REVERSE] Stack {key}: {inventory[key]}")
        inventory[key] = inventory[key][::-1]
        print(f"[REVERSING] Stack {key} is reversed {inventory[key]}")
    for line in f:
        line=line.strip("\n").split()
        n=int(line[1])
        from_stack = int(line[3])
        to_stack = int(line[-1])
        for i in range(n):
            print(f"[MOVING] Move {inventory[from_stack][-1]} from stack {from_stack} to stack {to_stack}")
            inventory[to_stack].append(inventory[from_stack].pop())
    for stack in inventory.keys():
        print(inventory[stack][-1])

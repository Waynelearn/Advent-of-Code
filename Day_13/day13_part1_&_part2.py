def right_order(left,right):
    #print(f"[STARTING] left:{left}:{type(left)},right:{right}:{type(right)}")
    if type(left) is list and type(right) is int:
        #print(f"[CONVERT RIGHT] {right}->{[right,]}")
        right = [right,]
    elif type(right) is list and type(left) is int:
        #print(f"[CONVERT LEFT] {left}->{[left,]}")
        left=[left,]
    #compare list
    if type(left) is list and right is None:
        #print("False because left is list and right is None")
        return False
    if left is None and type(right) is list:
        #print("True because left is None and right is list")
        return True
    if type(left) is list and type(right) is list:
        if len(left)==0 and len(right)!=0:
            #print("True because left list is empty and right list is not empty")
            return True
        elif len(right)==0 and len(left)!=0:
            #print("False because left list is not empty and right list is empty")
            return False
        elif len(right)==0 and len(left)==0:
            #print("NONE because left and right list have same length")
            pass
        else:
            idx=0
            #print(f"left:{left},right:{right}")
            #print(len(left)>0 and len(right)>0)
            while True:


                
                l=left[idx]
                r=right[idx]
                #print(f"[INSIDE WHILE LOOP]:left:{l}:type:{type(l)},right:{r}:type:{type(r)},index:{idx}")

                if type(l) is list and type(r) is int:
                    #print(f"[CONVERT R] {r}->{[r,]}")
                    r = [r,]
                elif type(r) is list and type(l) is int:
                    #print(f"[CONVERT L] {l}->{[l,]}")
                    l=[l,]

                #both list
                if type(l) is list and type(r) is list:
                    #print(f"[RECURSIVE CALL] left:{l},right:{r}")
                    if right_order(l,r):
                        #print("RECURSIVE CALL RETURNED TRUE")
                        return True
                    elif right_order(l,r) ==False:
                        #print("RECURSIVE CALL RETURNED FALSE")
                        return False

                    else:
                        #print("NOTHING HAPPENED-1")
                        pass
                
                
                #both int
                if type(l)==int and type(r)==int:
                    if l>r:
                        #print("False because left int is greater than right int")
                        return False
                    elif l<r:
                        #print("True because left int is less than right int")
                        return True
                    else:
                        #print("NOTHING HAPPENED-2")
                        pass
                
                if idx==len(left)-1 or idx==len(right)-1:
                    if len(left)==len(right):
                        #print(f"[BREAK] WHILE LOOP END: left:{left},right:{right}")
                        break
                    elif len(left)<len(right):
                        #print("True because len of right is longer")
                        return True
                    elif len(left)>len(right):
                        #print("False because len of left is longer")
                        return False
                idx+=1


        


left=[1,1,3,1,1]
right=[1,1,5,1,1]

left=[1,1]
right=[1,2]

left=[[]]
right=[[[]]]

left=[[1],[2,3,4]]
right=[[1],4]

left=[[4,4],4,4]
right=[[4,4],4,4,4]

left=[]
right=[3]

left=[1,[2,[3,[4,[5,6,7]]]],8,9]
right=[1,[2,[3,[4,[5,6,0]]]],8,9]
#print(right_order(left,right))

with open("input.txt","r") as f:
    data=[line.strip("\n") for line in f.readlines()]


import ast

parsed=[]
for line in data:
    if line != "":
        x=ast.literal_eval(line)
        x=[i for i in x]
        parsed.append(x)

total=0
pair_idx=1
for i in range(len(parsed)):
    if i%2==0:
        left=parsed[i]
        #print(f"left:{left}")
    elif i%2==1:
        right=parsed[i]
        #print(f"right:{right}")
        test=right_order(left,right)
        if test:
            total+=pair_idx
        #print(f"Pair_idx:{pair_idx}<------------------------------->,Correct order:{test}")
        pair_idx+=1
        

#print(total)

def bubble_sort(lst):
    array=lst.copy()
    for i in range(len(array)-1,-1,-1):
        for j in range(i):
            left=array[j]
            right=array[j+1]
            if right_order(left,right)==False:
                temp=array[j]
                array[j]=array[j+1]
                array[j+1]=temp
    return array




def binary_search(lst,key):
    max_idx=len(lst)
    min_idx=0
    idx=(min_idx+max_idx)//2
    curr=lst[idx]
    while True:
        #print(f"idx:{idx},curr:{curr},key:{key}")
        #is key smaller than curr
        if right_order(key,curr):
            max_idx=idx
            idx=(min_idx+max_idx)//2
            curr=lst[idx]
        elif right_order(key,curr)==False:
            min_idx=idx
            idx=(min_idx+max_idx)//2
            curr=lst[idx]
        else:
            return idx

parsed.extend([[[2]],[[6]]])
sorted_array=bubble_sort(parsed)

"""
for i in range(len(sorted_array)):
    if len(sorted_array[i])==1 and type(sorted_array[i][0]) is list and len(sorted_array[i][0])==1:
        print(i+1,sorted_array[i])
"""


print((binary_search(sorted_array,[[2]])+1)*(binary_search(sorted_array,[[6]])+1))






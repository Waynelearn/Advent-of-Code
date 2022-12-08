import string

with open("input.txt","r") as f:
    alphabet_to_num={string.ascii_letters[i]:i+1 for i in range(len(string.ascii_letters))}
    total=0
    idx=0
    group=[]
    for line in f:
        line=line.strip()
        if idx%3==0:
            shared=set(line)
        elif idx%3!=2:
            shared=shared.intersection(set(line))
        elif idx%3==2:
            shared=shared.intersection(set(line))
            total+=alphabet_to_num[list(shared)[0]]
        idx+=1
    print(total)
        
        
                         

import string

with open("input.txt","r") as f:
    alphabet_to_num={string.ascii_letters[i]:i+1 for i in range(len(string.ascii_letters))}
    total=0
    for line in f:
        line=line.strip()
        half=len(line)//2
        first=line[:half]
        second=line[half:]
        shared=list(set(first).intersection(set(second)))
        total+=alphabet_to_num[shared[0]]
    print(total)
        
        
                         

def max_arg(lst):
    m=-1
    idx=-1
    for i in range(len(lst)):
        if lst[i]>m:
            idx=i
            m=lst[i]
    return idx
with open("input.txt","r") as f:
    lst=[0,]
    idx=0
    for line in f.readlines():
        if line.strip() == "":
            lst.append(0)
            idx+=1
            continue
        lst[idx]+=int(line.strip())
    print(max_arg(lst)+1)
    print(lst[52])
    print(max(lst))

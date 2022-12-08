def max3_sum(lst):
    m1=-1
    m2=-1
    m3=-1
    for i in range(len(lst)):
        if lst[i]>m1:
            temp1=m1
            #replace m1 with larger num
            m1=lst[i]
            if temp1>m2:
                temp2=m2
                #replace m2 with prev m1
                m2=temp1
                if temp2>m3:
                    #replace m3 with prev m2
                    m3=temp2
            elif temp1>m3:
                m3=temp1
        elif lst[i]>m2:
            temp2=m2
            m2=lst[i]
            if temp2>m3:
                m3=temp2
    print(m1,m2,m3)
    return m1+m2+m3


with open("input.txt","r") as f:
    lst=[0,]
    idx=0
    for line in f.readlines():
        if line.strip() == "":
            lst.append(0)
            idx+=1
            continue
        lst[idx]+=int(line.strip())
    print(max3_sum(lst))
m1=max(lst)
lst.remove(m1)
m2=max(lst)
lst.remove(m2)
m3=max(lst)
print(m1)
print(m2)
print(m3)

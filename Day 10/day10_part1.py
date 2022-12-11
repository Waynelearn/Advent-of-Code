res=[]
val=1
cycle=0

with open("input.txt","r") as f:
    for line in f:
        line = line.strip("\n").split(" ")
        first=line[0]
        
        if first=="addx":
            
            second=int(line[1])
            for i in range(2):
                
                cycle+=1
                if (cycle-20)%40==0:
                    res.append(cycle*val)
                    print(f"cycle:{cycle},x:{val}")
                if i==1:
                    val+=second
        elif first=="noop":
            
            cycle+=1
            if (cycle-20)%40==0:
                res.append(cycle*val)
        if cycle>220:
            break
print(sum(res))
